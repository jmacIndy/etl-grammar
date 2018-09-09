# ./source_tables.py

import MySQLdb
import sys

class source_tables:

   def __init__(self, sourceInfo):

      self._name = sourceInfo.name
      self._description = sourceInfo.description
      self._connection = sourceInfo.connection
      self._column = sourceInfo.column

   def dumpSource(self):

      print '   -------------'
      print '      name      : %s - %s' % (self._name, self._description)
      print '      connection: %s' % (self._connection)
      for x in self._column:
         print '         column: %s %s' % (x.name, x.type)


