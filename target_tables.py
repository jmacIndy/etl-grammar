# ./target_tables.py

import MySQLdb
import sys

class target_tables:

   def __init__(self, targetInfo):

      self._name = targetInfo.name
      self._description = targetInfo.description
      self._connection = targetInfo.connection
      self._column = targetInfo.column

   def dumpTarget(self):

      print '   ------------'
      print '      name      : %s - %s' % (self._name, self._description)
      print '      connection: %s' % (self._connection)
      for x in self._column:
         print '         column: %s %s' % (x.name, x.type)


