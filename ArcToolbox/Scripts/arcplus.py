#@+leo-ver=5-thin
#@+node:maphew.20140522093157.1506: * @file arcplus.py
''' arcplus.py: functions missing from regular ol' arcpy module '''

import os
import arcpy
    

#@+others
#@+node:maphew.20140522093157.1509: ** listAllFeatureClasses
def listAllFeatureClasses (gdb,**kwargs):
    ''' list all Feature Classes in a geodatabase or coverage recursively (normal listFeatureClasses does not recurse)'''

    arcpy.env.workspace = gdb

    if not kwargs.has_key('fc_filter'): fc_filter = '*'
    else: fc_filter = kwargs ['fc_filter']

    if not kwargs.has_key('fd_filter'): fd_filter = '*'
    else: fd_filter = kwargs ['fd_filter']

    print 'Looking in %s for "%s" ' % (arcpy.env.workspace,fc_filter)

    fcs = []
    for fds in arcpy.ListDatasets(fd_filter,'feature') + ['']:
        for fc in arcpy.ListFeatureClasses(fc_filter,'',fds):
            #print '%s\\%s' % (fds,fc)
            fcs.append(os.path.join(fds,fc))

    return fcs
#@+node:maphew.20110314104726.3195: *3* extended docstring
'''
Optional keyword arguments, for example:

    fc_filter = 'HD_*', fd_filter = '*Hydro*

will process only feature classes that start with 'HD_' within feature datasets containing '*Hydro*'

Thank you Gotchula:
@url http://gis.stackexchange.com/questions/5893/list-all-feature-classes-in-gdb-including-within-feature-datasets
and http://stackoverflow.com/questions/3394835/args-and-kwargs
'''
#@-others
#@-leo
