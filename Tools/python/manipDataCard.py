#!/usr/bin/env python
import sys,os,inspect
from optparse import OptionParser
from copy import deepcopy as dc

class card():
	'''Class card() is intended to contain a datacard, structured in a couple of dictionaries for simplified editing.'''
#FUNCTION: init###################################
	def __init__(self,cardName='dataCard.txt'):
		'''Method __init__(cardName) takes as input the file name of the card to read from.'''
		self.cardName = cardName
##################################################
#open
		self.card = open(cardName,'r+')
		self.content = {}
		self.content['header1'] = {}		# imax, ... lines
		self.content['header2'] = {}		# shapes lines
		self.content['block1'] = {}			# bin/observation lines
		self.content['block2'] = {}			# bin/process/rate lines
		self.content['systs'] = {}			# systematic blocks
		# keep track of general position in file 
		self.advance = [False,False,False,False,False] #header1, header2, block1, block2, systs
		self.done = [False,False,False,False,False]
		# keep track of original line numbers
		self.linenumbers = {}
		# keep track of substituted dictionary keys
		self.substitutes = {'processId':'process'}
#parse
		self.lines = {}
		iline = 0
		for line in self.card.read().split('\n'):
			if line == '': continue
			if '-----' in line: continue
			if line[0] == '#': continue
			self.lines[iline] = line
			iline += 1
#close
		self.card.close()
##################################################
#parse
		ih2 = 0
		prevTag = ''
		currTag = ''
		for iline, (kline, line) in enumerate(self.lines.iteritems()):
			fields = line.split()
			currTag = fields[0]
			if currTag == 'Observation': currTag = 'observation'
			if prevTag == 'Observation': prevTag = 'observation'
			# whereAmI
			if not kline > len(self.lines.keys())-4:
				nextfour = [currTag,self.lines[kline+1].split()[0],self.lines[kline+2].split()[0],self.lines[kline+3].split()[0]]
			else:
				nextfour = ['','','','']
		####################	
			if set(nextfour[0:3]) == set(['imax','jmax','kmax']):
				#print "\033[31mCASE HEADER1\033[m"
				self.advance[0] = True
				self.advance[1] = False
				self.advance[2] = False
				self.advance[3] = False
				self.advance[4] = False
				self.done[0] = True
			elif set(nextfour[0:2]) == set(['bin','observation']) and not self.done[2] and len(fields)==len(self.lines[kline+1].split()):
				#print "\033[31mCASE BLOCK1\033[m"
				self.advance[0] = False
				self.advance[1] = False
				self.advance[2] = True
				self.advance[3] = False
				self.advance[4] = False
				self.done[2] = True
			elif nextfour[0] == 'observation' and not self.done[2]:
				#print "\033[31mCASE BLOCK1\033[m"
				self.advance[0] = False
				self.advance[1] = False
				self.advance[2] = True
				self.advance[3] = False
				self.advance[4] = False
				self.done[2] = True
			elif set(nextfour) == set(['bin','process','process','rate']):
				#print "\033[31mCASE BLOCK2\033[m"
				self.advance[0] = False
				self.advance[1] = False				
				self.advance[2] = False
				self.advance[3] = True
				self.advance[4] = False
				self.done[1] = True  # for cases where there are no shapes lines 
			elif currTag == 'shapes' and not self.done[1]:
				#print "\033[31mCASE HEADER1\033[m"
				self.advance[0] = False
				self.advance[1] = True
				self.advance[2] = False
				self.advance[3] = False
				self.advance[4] = False
				self.done[1] = True
				ih2 = 0
			elif all(self.done[0:4]):
				#print "\033[31mCASE SYSTS\033[m"
				self.advance[0] = False
				self.advance[1] = False
				self.advance[2] = False
				self.advance[3] = False
				self.advance[4] = True
		####################	
			# header1
			#if currTag in ['imax','jmax','kmax']:
			if self.advance[0]:
				#self.advance[0] = True
				self.content['header1'][currTag] = fields[1]
				self.linenumbers[('header1',currTag)] = iline
			# header2
			#elif currTag in ['shapes']:
			elif self.advance[1]:
				#self.advance[1] = True
				self.content['header2'][str(ih2)] = fields
				self.linenumbers[('header2',str(ih2))] = iline
				ih2 += 1
			# block1
			#elif currTag == 'bin' and not prevTag == 'observation':
			elif self.advance[2]:
				#self.advance[2] = True
				if not currTag in self.content['block1']:
					self.content['block1'][currTag] = fields[1:] 
					self.linenumbers[('block1',currTag)] = iline
				else: sys.exit('Key %s already exists in block1 dictionary. \nNo algorithm to process line: %s'%(currTag,line))
			# block2
			#elif currTag == 'bin' and prevTag == 'observation':
			elif self.advance[3]:
				#self.advance[3] = True
				if not currTag in self.content['block2']:
					self.content['block2'][currTag] = fields[1:] 
					self.linenumbers[('block2',currTag)] = iline
				elif currTag == 'process' and 'process' in self.content['block2']:
					self.content['block2']['processId'] = fields[1:]
					self.linenumbers[('block2','processId')] = iline
				else: sys.exit('Key %s already exists in block2 dictionary. \nNo algorithm to process line: %s'%(currTag,line))
				if set(self.content['block2'].keys()) == set(['bin','process','processId','rate']):
					self.done[3] = True
					if not 'bin' in self.content['block1']:
						if len(set(self.content['block2']['bin'])) > 1:
							sys.exit('More than one bintype requires specific bin line together with observation line. Please add it.')
						self.content['block1']['bin'] = list(set(self.content['block2']['bin']))
						self.linenumbers[('block1','bin')] = str(float(self.linenumbers[('block1','observation')])-0.01)
			# systs 
			elif self.advance[4]:
				parsed = False
				for systtype in ['lnN','lnU','shape','gmN','param','rateParam']:
					if fields[1] == systtype or fields[1][0:5] == systtype:
						# append if new
						if not fields[1] in self.content['systs']: self.content['systs'][fields[1]] = {}
						# fill
						self.content['systs'][fields[1]][currTag] = fields[2:]
						# track line numbers			
						self.linenumbers[(fields[1],currTag)] = iline
						parsed = True
						break
				if not parsed:
						sys.exit('No algorithm to process line: %s with key %s'%(line, fields[1]))
			# other
			else: #sys.exit('Problem parsing line: %s'%line)
                          print 'Warning: Problem parsing line: ' , line

			prevTag = currTag
		
##################################################
	def addShape(self,name,number,root,workspace,hist=''):
		'''Method addShape() takes as input the 4 elements usually on a shapes line.'''
		n = str(max([int(x) for x in self.content['header2']])+1)
		self.content['header2'][n] = ['shapes',name,number,root,workspace,hist]
		self.linenumbers[('header2',n)] = self.linenumbers[('header2',str(int(n)-1))] + 0.01

##################################################
	def remShape(self,label,root='ALL'):
		if not (not label == '' and not root == ''):
			sys.exit('Arguments don\'t suffice, check these: label: '+str(label)+', root: '+str(root))
		for key in self.content['header2'].keys():
			fields = self.content['header2'][key]
			if (fields[1] == label and fields[2] == root) or (fields[1] == label and root == 'ALL'):
				del self.content['header2'][key]
				print 'removed:', fields

##################################################
	def addCol(self,bin,process,processId,rate,observation):
		'''Method addCol() takes as input all the information in a column in block1 (bin/observation) and block2 (bin/process/rate), as well as adds the extra column to the systematics blocks where needed.'''
		#block1
                if not str(bin) in self.content['block1']['bin']:
		  self.content['block1']['bin'].append(str(bin))
		  self.content['block1']['observation'].append(str(observation))
		#block2
		self.content['block2']['bin'].append(str(bin))
		self.content['block2']['process'].append(str(process))
		self.content['block2']['processId'].append(str(processId))
		self.content['block2']['rate'].append(str(rate))
		#systs
		for systtype in self.content['systs']:
			if systtype in ['lnN','lnU','gmN','shape'] or systtype[0:5] == 'shape':
				for entry in self.content['systs'][systtype].itervalues():
					entry.append('-')
		#header1
		self.content['header1']['imax'] = str(len(set(self.content['block1']['bin'])))

#FUNCTION: delCol################################
	def remCol(self,**kwargs):
		'''Method remCol.'''
		sets = [['bin','process'],['bin','processId'],['bin'],['process'],['processId']]
		iset = -999
		for i,s in enumerate(sets):
			if (set(s)).issubset(kwargs.keys()):
				iset = i
				break
		if iset == -999:
			sys.exit('Not enough information. Check arguments: '+str(kwargs))
		if iset == 2:
			if not kwargs['bin'] in self.content['block2']['bin']:
				sys.exit('No such bin in card, can\'t remove. Check arguments: '+str(kwargs))
			allprocesses = dc(self.content['block2']['process'])
			for process in allprocesses:
				if self.content['block2']['bin'][self.content['block2']['process'].index(process)] == kwargs['bin']:
					self.remCol(bin=kwargs['bin'],process=process)
		elif iset == 3:
			if not kwargs['process'] in self.content['block2']['process']:
				sys.exit('No such process in card, can\'t remove. Check arguments: '+str(kwargs))
			allprocesses = dc(self.content['block2']['process'])
			for process in allprocesses:
				if process == kwargs['process']:
					self.remCol(bin=self.content['block2']['bin'][self.content['block2']['process'].index(process)],process=process)
		elif iset == 4:
			if not kwargs['processId'] in self.content['block2']['processId']:
				sys.exit('No such processId in card, can\'t remove. Check arguments: '+str(kwargs))
			allprocesses = dc(self.content['block2']['processId'])
			for processid in allprocesses:
				if processid == kwargs['processId']:
					self.remCol(bin=self.content['block2']['bin'][self.content['block2']['processId'].index(processid)],processId=processid)
		else:
			print 'REMOVING: ',kwargs
			#start
			index1 = self.commonIndex(part='block1',bin=kwargs[sets[iset][0]])
			if 'process' in kwargs:
				index2 = self.commonIndex(part='block2',bin=kwargs[sets[iset][0]],process=kwargs[sets[iset][1]])
			elif 'processId' in kwargs:
				index2 = self.commonIndex(part='block2',bin=kwargs[sets[iset][0]],processId=kwargs[sets[iset][1]])
			#block2
			del self.content['block2']['bin'][index2]
			del self.content['block2']['process'][index2]
			del self.content['block2']['processId'][index2]
			del self.content['block2']['rate'][index2]
			#systs
			for systtype in self.content['systs']:
				if systtype in ['lnN','lnU','gmN','shape'] or systtype[0:5] == 'shape':
					for tag in self.content['systs'][systtype]:
						del self.content['systs'][systtype][tag][index2 if not systtype=='gmN' else index2+1]
					remtags = []
					for tag in self.content['systs'][systtype]:
						if (not systtype=='gmN') and all([x=='-' for x in self.content['systs'][systtype][tag]]):
							remtags.append([systtype,tag])
						if (systtype=='gmN') and all([x=='-' for x in self.content['systs'][systtype][tag][1:]]):
							remtags.append([systtype,tag])
					for systtype,tag in remtags:
						print 'removed syst for tag %s: '%tag, self.content['systs'][systtype][tag]
						del self.content['systs'][systtype][tag]

			#block1
			allbins = dc(self.content['block1']['bin'])
			for entry in allbins:
				if not entry in self.content['block2']['bin']:
					del self.content['block1']['observation'][self.content['block1']['bin'].index(entry)]
					del self.content['block1']['bin'][self.content['block1']['bin'].index(entry)]
					self.content['header1']['imax'] = str(int(self.content['header1']['imax'])-1)
				
#FUNCTION: getCol################################
	def getCol(self,**kwargs):
		'''Method getCol.'''
		sets = [['bin','process'],['bin','processId']]
		iset = -999
		for i,s in enumerate(sets):
			if (set(s)).issubset(kwargs.keys()):
				iset = i
				break
		if iset == -999:
			sys.exit('Not enough information. Check arguments: '+str(kwargs))
		#start
		index1 = self.commonIndex(part='block1',bin=kwargs[sets[iset][0]])
		if 'process' in kwargs:
			index2 = self.commonIndex(part='block2',bin=kwargs[sets[iset][0]],process=kwargs[sets[iset][1]])
		elif 'processId' in kwargs:
			index2 = self.commonIndex(part='block2',bin=kwargs[sets[iset][0]],processId=kwargs[sets[iset][1]])
		passcontent = {}
		#block1
		passcontent['block1'] = {}
		passcontent['block1']['bin'] = self.content['block1']['bin'][index1]
		passcontent['block1']['observation'] = self.content['block1']['observation'][index1]
		#block2
		passcontent['block2'] = {}
		passcontent['block2']['bin'] = self.content['block2']['bin'][index2]
		passcontent['block2']['process'] = self.content['block2']['process'][index2]
		passcontent['block2']['processId'] = self.content['block2']['processId'][index2]
		passcontent['block2']['rate'] = self.content['block2']['rate'][index2]
		#systs
		passcontent['systs'] = {}
		for systtype in ['lnN','gmN','lnU','shape']:
			if not systtype in self.content['systs']: continue
			passcontent['systs'][systtype] = {}
			for tag in self.content['systs'][systtype]:
				passcontent['systs'][systtype][tag] = self.content['systs'][systtype][tag][index2 if not systtype=='gmN' else index2+1]
		return passcontent

#FUNCTION: setCol################################
	def setCol(self,**kwargs):
		'''Method setCol().'''
		if not 'content' in kwargs:
			sys.exit('Can\'t create new FILLED column if you don\'t pass content. Add content=... .')
		#start
		passedcontent = kwargs['content']
		#block1
		if not (('bin' in kwargs) and ('process' in kwargs or 'processId' in kwargs)):
			if passedcontent['block1']['bin'] in self.content['block1']['bin']:
				sys.exit('Bin label %s already exists in dictionary. Rename with bin+process+processId.'%passedcontent['block1']['bin'])
			self.content['block1']['bin'].append(str(passedcontent['block1']['bin']))
		else:
			self.content['block1']['bin'].append(str(kwargs['bin']))
		self.content['block1']['observation'].append(str(passedcontent['block1']['observation']))
		#block2
		if not (('bin' in kwargs) and ('process' in kwargs or 'processId' in kwargs)):
			if passedcontent['block2']['bin'] in self.content['block2']['bin']:
				indices = [i for i in range(len(self.content['block2']['bin'])) if self.content['block2']['bin'][i] == passedcontent['block2']['bin']]
				for i in indices:
					if self.content['block2']['process'][i] == passedcontent['block2']['process']:
						sys.exit('(bin,process):(%s,%s) already exists in dictionary. Rename with bin+process+processId.'%(passedcontent['block2']['bin'],passedcontent['block2']['process']))
			self.content['block2']['bin'].append(str(passedcontent['block2']['bin']))
			self.content['block2']['process'].append(str(passedcontent['block2']['process']))
			self.content['block2']['processId'].append(str(passedcontent['block2']['processId']))
		else:
			if (not 'processId' in kwargs) or (not 'process' in kwargs):
				sys.exit('Defining new names needs full set bin/process/processId. Check arguments: '+str(kwargs))
			self.content['block2']['bin'].append(str(kwargs['bin']))
			self.content['block2']['process'].append(str(kwargs['process']))
			self.content['block2']['processId'].append(str(kwargs['processId']))
		self.content['block2']['rate'].append(str(passedcontent['block2']['rate']))
		#systs	
		lookatsysts = ['lnN','lnU','gmN','shape']
		for systtype in self.content['systs']:
			if not (systtype in lookatsysts or systtype[0:5]=='shape'): continue
			for entry in self.content['systs'][systtype]:
				if systtype in passedcontent['systs']:
					if entry in passedcontent['systs'][systtype]:
						self.content['systs'][systtype][entry].append(passedcontent['systs'][systtype][entry])
					else:
						self.content['systs'][systtype][entry].append('-')
						#print 'No input for %s - %s'%(systtype, entry)
				else:
					self.content['systs'][systtype][entry].append('-')
					#print 'No input for %s'%systtype
		for systtype in passedcontent['systs']:
			if not (systtype in lookatsysts or systtype[0:5]=='shape'): continue
			if not systtype in self.content['systs']:
				self.content['systs'][systtype] = {}
				nfrom = max([float(x) for x in self.linenumbers.itervalues()])
				for entry in passedcontent['systs'][systtype]:
#					print 'Also found %s info in input set. Skipping.'%systtype
					self.content['systs'][systtype][entry] = ['-']*(len(self.content['block2']['bin'])-1)+[passedcontent['systs'][systtype][entry]]
					nfrom += 1
					self.linenumbers[(systtype,entry)] = str(nfrom)
			else:
				for entry in passedcontent['systs'][systtype]:
					nfrom = max([float(x) for x in self.linenumbers.itervalues()])
					if not entry in self.content['systs'][systtype]:
#						print 'Also found %s - %s info in input set. Skipping'%(systtype,entry)
						self.content['systs'][systtype][entry] = ['-']*(len(self.content['block2']['bin'])-1)+[passedcontent['systs'][systtype][entry]]
						nfrom += 0.01
						self.linenumbers[(systtype,entry)] = str(nfrom)
		#header1
		self.content['header1']['imax'] = str(len(set(self.content['block1']['bin'])))

#FUNCTION: commonIndex################################
	def commonIndex(self,**kwargs):
		'''Method commonIndex() is internally used to determine array indices.'''
		# checks
		if not 'part' in kwargs:
			sys.exit('Not enough arguments to determine index. Check these: '+str(kwargs))
		if kwargs['part'] == 'block1':
			if not ('bin' in kwargs):
				sys.exit('Not enough arguments to determine index. Check these: '+str(kwargs))
		elif kwargs['part'] == 'block2':
			if not ('process' in kwargs or 'processId' in kwargs) or not ('bin' in kwargs):
				sys.exit('Not enough arguments to determine index. Check these: '+str(kwargs))
		else:
				sys.exit('Not enough arguments to determine index. Check these: '+str(kwargs))
		ind1 = []
		ind2 = []
		# index determination
		# block1
		if kwargs['part'] == 'block1':
			for ientry,entry in enumerate(self.content['block1']['bin']):
				if entry == kwargs['bin']:
					ind1 += [ientry]
			if len(ind1)>1:
				sys.exit('No unique index found. Check indices: %s and arguments: '%str(indices)+str(kwargs))
			indices = ind1
		# block2
		elif kwargs['part'] == 'block2':
			for ientry,entry in enumerate(self.content['block2']['bin']):
				if entry == kwargs['bin']:
					ind1 += [ientry]
			if 'process' in kwargs:
				for ientry,entry in enumerate(self.content['block2']['process']):
					if entry == kwargs['process']:
						ind2 += [ientry]
			elif 'processId' in kwargs:
				for ientry,entry in enumerate(self.content['block2']['processId']):
					if entry == kwargs['processId']:
						ind2 += [ientry]
			indices = list(set(ind1).intersection(ind2))
			if len(indices)>1:
				sys.exit('No unique index found. Check indices: %s and arguments: '%str(indices)+str(kwargs))
		# other
		else:
			sys.exit('Problem with argument. Check these: '+str(kwargs))
		# final
		return indices[0]

##################################################
	def colwidth(self,part,field,syst='',systfield=-1):
		'''Method colwidth() is used internally for formatted printing.'''
		if not part == 'systs':
			if not field == 0:
				total = [len(x) for x in [y[(field-1)] for y in self.content[part].itervalues() if (len(y) > (field-1))]]
			else:
				total = [len(x) for x in self.content[part]]
		else:
			if not field == 0:
				total = [len(x) for x in [y[(field-1)] for y in self.content[part][syst].itervalues() if (len(y) > (field-1))]]
			else:
				if systfield==0:
					total = [len(x) for x in self.content[part][syst]]
				elif systfield==1:
					total = [len(syst)]
		m = max(total)
		return m 

##################################################
#FUNCTION: getIndex###############################
	def getIndex(self,**kwargs):
		'''Method getIndex() is used internally for retrieving array indices based on dictionary keys.'''
		sets = [['tag','syst','bin','process'],['tag','syst','bin','processId'],['tag','syst','col'],['bin','process'],['bin','processId']]
		iset = -1
		i3 = sets.index(['tag','syst','col'])
		i2 = sets.index(['bin','process'])
		for i,s in enumerate(sets):
			if (set(s)).issubset(kwargs.keys()):
				iset = i
				break
		if (iset < 0) or (iset >= i2 and 'syst' in kwargs): 
			sys.exit('Not enough arguments to identify which value to set. Correct these: '+str(kwargs))
		# rate case
		if iset >= i2 and iset < len(sets):
			for ix1,x1 in enumerate(self.content['block2'][sets[iset][0]]):
				if not x1 == kwargs[sets[iset][0]]: continue
				if not self.content['block2'][sets[iset][1]][ix1] == kwargs[sets[iset][1]]: continue
				index = ix1
			return index, sets[iset]
		# syst cases (many cols)
		elif iset < i3:
			for ix1,x1 in enumerate(self.content['block2'][sets[iset][2]]):
				if not x1 == kwargs[sets[iset][2]]: continue
				if not self.content['block2'][sets[iset][3]][ix1] == kwargs[sets[iset][3]]: continue
				index = (ix1 if not kwargs['syst']=='gmN' else ix1+1)
			return index, sets[iset]
		# syst cases (two cols)
		elif iset >= i3 and iset < i2:
			if not kwargs['col'] in [0,1]:
				sys.exit('Column value has to be 0 (mean) or 1 (sigma).')
			index = kwargs['col']
			return index, sets[iset]
		else:
			sys.exit('Something is wrong with the arguments. Check these: '+str(kwargs))

#FUNCTION: getRate################################
	def getRate(self,**kwargs):
		'''Method getRate() can be used to retrieve a rate from block2, by inputting either (bin, process) or (bin, processId) in the format (bin=..., process=...).'''
		index,keyset = self.getIndex(**kwargs)
		return self.content['block2']['rate'][index]

#FUNCTION: setRate################################
	def setRate(self,**kwargs):
		'''Method setRate() can be used to set a rate in block2, by inputting either (bin, process) or (bin, processId) in the format (bin=..., process=...) + the intended value as (,value=...).'''
		if not 'value' in kwargs: sys.exit('No value specified to set.')
		index,keyset = self.getIndex(**kwargs)
		self.content['block2']['rate'][index] = str(kwargs['value'])

#FUNCTION: getSyst################################
	def getSyst(self,**kwargs):
		'''Method getSyst() can be used to retrieve a systematic from the systs block, by inputting either (tag, syst, bin, process) or (tag, syst, bin, processId) in the format (tag=..., syst=..., bin=..., process=...) when considering systematics of type (lnN, lnU, gmN or shape), or by inputting (tag, syst, col) when considering systematics of type (param).'''
		index,keyset = self.getIndex(**kwargs)
		return self.content['systs'][kwargs[keyset[1]]][kwargs[keyset[0]]][index]

#FUNCTION: setSyst################################
	def setSyst(self,**kwargs):
		'''Method setSyst() can be used to set a systematic in the systs block, by inputting either (tag, syst, bin, process) or (tag, syst, bin, processId) in the format (tag=..., syst=..., bin=..., process=...) when considering systematics of type (lnN, lnU, gmN or shape), or by inputting (tag, syst, col) when considering systematics of type (param) + the intended value as (,value=...).'''
		if not 'value' in kwargs: sys.exit('No value specified to set.')
		index,keyset = self.getIndex(**kwargs)
		self.content['systs'][kwargs[keyset[1]]][kwargs[keyset[0]]][index] = str(kwargs['value'])

##################################################
	def setgmN0(self,tag,value):
		if not 'gmN' in self.content['systs']:
			sys.exit('No gmN section in dictionary.')
		if not tag in self.content['systs']['gmN']:
			sys.exit('No tag: %s in gmN section in dictionary.'%tag)
		self.content['systs']['gmN'][tag][0] = str(value)

##################################################
	def remSystLine(self,**kwargs):
		sets = [['systtype','tag'],['tag']]
		iset = -999
		for i,s in enumerate(sets):
			if (set(s)).issubset(kwargs.keys()):
				iset = i
				break
		if iset == -999:
			sys.exit('Not enough information. Check arguments: '+str(kwargs))
		# check
		if iset == 0:
			if not kwargs['systtype'] in self.content['systs']:
				sys.exit('Systtype: %s is not present in the dictionary.'%kwargs['systtype'])
			if not kwargs['tag'] in self.content['systs'][kwargs['systtype']]:
				sys.exit('Tag: %s is not present in the dictionary.'%kwargs['tag'])
			del self.content['systs'][kwargs['systtype']][kwargs['tag']]
		elif iset == 1:
			tagfound = False
			systtypefound = ''
			for systtype in self.content['systs']:
				if kwargs['tag'] in self.content['systs']:
					tagfound=True
					systtypefound=systtype
					break
			if not tagfound:
				sys.exit('Tag: %s is not present in the dictionary.'%kwargs['tag'])
			del self.content['systs'][systtypefound][kwargs['tag']]
		else:
			sys.exit('Something is wrong. Check arguments: '+str(kwargs))
		
##################################################
	def addSystLine(self,**kwargs):
		sets = [['systtype','tag']]
		iset = -999
		for i,s in enumerate(sets):
			if (set(s)).issubset(kwargs.keys()):
				 iset = i
				 break
		if iset == -999:
			sys.exit('Not enough information. Check arguments: '+str(kwargs))
		# check preexisting
		for systtype in self.content['systs']:
			for tag in self.content['systs'][systtype]:
				if kwargs['tag'] == tag:
					sys.exit('Systematic line with tag %s already exists, in systematic section: %s'%(tag,systtype))
		# check type
		if not (kwargs['systtype'] in ['lnN','lnU','gmN','param']) and not (kwargs['systtype'][0:5]=='shape'):
			sys.exit('Systtype: %s is unknown in dictionary.'%systtype)
		# make new line:
		if kwargs['systtype'] == 'param':
			if not kwargs['systtype'] in self.content['systs']: self.content['systs'][kwargs['systtype']] = {}
			self.content['systs'][kwargs['systtype']][kwargs['tag']] = ['-']*2
			if kwargs['systtype'] in [x for x,y in self.linenumbers]: 
				self.linenumbers[(kwargs['systtype'],kwargs['tag'])] = str(  max(  [float(self.linenumbers[(x,y)]) for x,y in self.linenumbers.keys() if x == kwargs['systtype']]  )+0.01  )
			else:
				self.linenumbers[(kwargs['systtype'],kwargs['tag'])] = str(max([float(self.linenumbers[(x,y)]) for x,y in self.linenumbers if x == 'param'])+10)
		elif kwargs['systtype'] in ['lnN','lnU','gmN'] or kwargs['systtype'][0:5]=='shape':
			if not kwargs['systtype'] in self.content['systs']: self.content['systs'][kwargs['systtype']] = {}
			linelen = len(self.content['block2']['process'])
			self.content['systs'][kwargs['systtype']][kwargs['tag']] = (['-'] if kwargs['systtype']=='gmN' else [])+['-']*linelen
			if kwargs['systtype'] in [x for x,y in self.linenumbers]:
				self.linenumbers[(kwargs['systtype'],kwargs['tag'])] = str(max([float(self.linenumbers[(x,y)]) for x,y in self.linenumbers if x == kwargs['systtype']])+0.01)
			else:
				self.linenumbers[(kwargs['systtype'],kwargs['tag'])] = str(max([float(self.linenumbers[(x,y)]) for x,y in self.linenumbers if x == 'param'])+10)
		else:
			sys.exit('Something is wrong. Check arguments: '+str(kwargs))

##################################################
#FUNCTION: write##################################
	def write(self,cardNameOut=''):
		'''Method write() print the card in memory to the screen, or to a file if a filename is specified.'''
# destination
		if not cardNameOut == '':
			if os.path.exists(cardNameOut):
				sys.exit('File %s already exists. NOT overwriting.'%cardNameOut)
			f_out = open(cardNameOut,'w+')
			sys.stdout = f_out
# header1 - header2 - block1 - block2
		for part in ['header1','header2','block1','block2']: 
			if not part == 'header2':
				for key in sorted(self.content[part], key=lambda x:float(self.linenumbers[(part,x)])):
					form = '%%-%is'%(self.colwidth(part,0)+1)
					print form%(key if not key in self.substitutes else self.substitutes[key]),
					for ifield,field in enumerate(self.content[part][key]):
						form = '%%%is'%(self.colwidth(part,ifield+1)+1)
						print form%field,
					print
			else:
				for key in sorted(self.content[part], key=lambda x:float(self.linenumbers[(part,x)])):
					for ifield,field in enumerate(self.content[part][key]):
						if ifield == 0:
							form = '%%-%is'%(self.colwidth(part,ifield+1)+1)
						else:
							form = '%%%is'%(self.colwidth(part,ifield+1)+1)
						print form%field,
					print
			print '-'*30
# systs
		for syst in sorted(self.content['systs'], key=lambda x:min([self.linenumbers[y] for y in self.linenumbers.keys() if y[0]==x])):
			for key in sorted(self.content['systs'][syst], key=lambda x:float(self.linenumbers[(syst,x)])):
				form = '%%-%is'%(self.colwidth('systs',0,syst,0)+1)
				print form%key, 
				form = '%%%is'%(self.colwidth('systs',0,syst,1)+1)
				print form%syst,
				for ifield,field in enumerate(self.content['systs'][syst][key]):
					form = '%%%is'%(self.colwidth('systs',ifield+1,syst)+1)
					print form%field,
				print
			print '-'*30
# reset defaults and close file if needed
		if not cardNameOut == '':
			f_out.close()
			sys.stdout = sys.__stdout__

####################################################################################################
####################################################################################################
####################################################################################################
####################################################################################################
####################################################################################################
def info(text):
	print '\033[31m*'*(len(text)+4)
	print '* '+text+' *'
	print '*'*(len(text)+4)+'\033[m'

def makebreak(n=3):
	for i in range(n):
		print '\033[1;31m'+'&'*180+'\033[m'

####################################################################################################
def demo0():
	dc = card('datacard_mbbCor_m115_CATMIN1_Binned_adapted.txt')
	####################
	info('Example printout of scanned card:')
	dc.write()
	print
	####################
	info('Example of reading and setting rate:')
	print 'read CAT1, signal, rate: \t', dc.getRate(bin='CAT1', process='signal')
	print 'read CAT1, 0, rate: \t', dc.getRate(bin='CAT1', processId='0')
	print 'read CAT1, background, rate: \t', dc.getRate(bin='CAT1', process='background')
	print 'set CAT1, background, rate to 1.111'
	dc.setRate(bin='CAT1', process='background',value='1.111')
	print 'read CAT, background, rate: \t', dc.getRate(bin='CAT1', process='background')
	print
	####################
	info('Example of reading and setting systematic (lnN):')
	print 'read CAT1, signal, lnN, lumi:\t', dc.getSyst(bin='CAT1', process='signal', syst='lnN', tag='lumi')
	print 'read CAT3, signal, lnN, trigEff:\t', dc.getSyst(bin='CAT3', process='signal', syst='lnN', tag='trigEff')
	print 'read CAT3, 0, lnN, trigEff:\t', dc.getSyst(bin='CAT3', processId='0', syst='lnN', tag='trigEff')
	print 'set CAT3, 0, lnN, trigEff to 1.111'
	dc.setSyst(bin='CAT3', processId='0', syst='lnN', tag='trigEff',value='1.111')
	print 'read CAT3, 0, lnN, trigEff:\t', dc.getSyst(bin='CAT3', processId='0', syst='lnN', tag='trigEff')
	print
	####################
	info('Example of reading and setting systematic (gmN):')
	print 'read CAT1, signal, gmN, blablabla: \t', dc.getSyst(bin='CAT1', process='signal', syst='gmN', tag='blablabla')
	print 
	####################
	info('Example of reading and setting systematic (param):')
	print 'read nzjet_CAT1, column 0: \t', dc.getSyst(syst='param',tag='nzjet_CAT1',col=0)
	print 'set nzjet_CAT1, column 0 to 9.9999'
	dc.setSyst(syst='param',tag='nzjet_CAT1',col=0,value='9.9999')
	print 'read nzjet_CAT1, column 0: \t', dc.getSyst(syst='param',tag='nzjet_CAT1',col=0)
	print
	####################
	info('Example of adding shape:')
	dc.addShape('signal2','*','bla','blablabla')
	print
	####################
	info('Example of adding column:')
	dc.addCol('CAT5','signal','0','22.55','-1')
	dc.addCol('CAT5','background','1','33.44','-1')
	####################
	info('Example of filling new column:')
	dc.setSyst(bin='CAT5', process='signal',syst='lnN',tag='trigEff',value='1.033')
	dc.setSyst(bin='CAT5', process='signal',syst='lnN',tag='lumi',value=dc.getSyst(bin='CAT1',process='signal',syst='lnN',tag='lumi'))
	print
	####################
	info('Example printout of edited card (to screen):')
	dc.write()
	#####################
	#info('Example printout of edited card (to dataCard_new.txt):')
	#dc.write('dataCard_new.txt')
	print
	####################
	info('Example getCol()')
	dc.setCol(content=dc.getCol(bin='CAT1',process='signal',processId='0'),bin='CAT17',process='signal',processId='0')
	dc.write()

####################################################################################################
def demo1():
	dc = card('hww-19.47fb.mH110.sf_vh2j_shape.txt')
	dc2 = card('hwwsf_0j_cut_7TeV.txt')
	info('examples of reading card')
	print 'read sf_vh2j, ggH, CMS_8TeV_eff_l, shape', dc.getSyst(bin='sf_vh2j',process='ggH', syst='shapeN2', tag='CMS_8TeV_eff_l')
	print 'read sf_vh2j, ggH, Gen_pow_WW, shape', dc.getSyst(bin='sf_vh2j',process='WW', syst='shapeN2', tag='Gen_pow_WW')
	print 'read sf_vh2j, ggH, Gen_pow_WW, shape', dc.getSyst(bin='sf_vh2j',process='VV', syst='shapeN2', tag='Gen_pow_WW')
	print
	info('examples of adding columns')
	print 'adding column of dc2 to dc (new names):'
	dc.setCol(content=dc2.getCol(bin='j0sf7tev',process='ZH'),bin='addedbin',process='addedprocess',processId='99')
	print 'adding column of dc2 to dc (orig names):'
	dc.setCol(content=dc2.getCol(bin='j0sf7tev',process='ZH'))
	dc.write()

####################################################################################################
def demo2():
	dc = card('hwwsf_0j_cut_7TeV.txt')
	dc.write()

####################################################################################################
def demo3():
	dc = card('hww-19.47fb.mH110.sf_vh2j_shape.txt')
	dc.write()
	dc.remShape('data_obs','*') # or remShape('data_obs')  (= remove everything with data_obs inside)
	dc.write()

####################################################################################################
def demo4():
	dc = card('hww-19.47fb.mH110.sf_vh2j_shape.txt')
	dc.write()
	dc.remCol(process='WW')
	dc.write()
	dc.remCol(processId='2')
	dc.write()

####################################################################################################
def demo5():
	dc = card('datacard_mbbCor_m115_CATMIN1_Binned.txt')
	dc.write()
	dc.addSystLine(systtype='param',tag='systparam')
	dc.write()
	dc.addSystLine(systtype='gmN',tag='systgmN')
	dc.setgmN0('systgmN','12.5')
	dc.write()
	dc.addSystLine(systtype='shapeN2',tag='systshapeN2')
	dc.write()
	dc.addSystLine(systtype='lnN',tag='systlnN')
	dc.write()
	dc.remSystLine(systtype='lnN',tag='sgnAcc_pdf')
	dc.write()

####################################################################################################
def myparser():
	mp = OptionParser()
	mp.add_option('--help_card',help='print info on how to use card class.',action='store_true',default=False,dest='help_card')
	return mp

####################################################################################################
def main():
	#demo0()
	#makebreak()
	#demo1()
	#makebreak()
	#demo2()
	#makebreak()
	#demo3()
	#makebreak()
	#demo4()
	#makebreak()
	demo5()

####################################################################################################
if __name__=='__main__':
	mp = myparser()
	opts,args = mp.parse_args()
	if opts.help_card:
		help(card)
		sys.exit(0)
	main()
