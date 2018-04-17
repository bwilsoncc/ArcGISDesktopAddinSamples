from __future__ import print_function
import arcpy
from datetime import date
import os

class AttrUpdate(object):
    """description of class"""

    def __init__(self, fc):
        self.fc = fc

    def update_auto(self, fid):
        """ Update the AUTO* fields if they exist """

        print("Updating %d in %s" % (fid,self.fc))

        d = arcpy.Describe(self.fc)
        oidfield = d.OIDFieldName
        fields = [ fld.name for fld in d.fields ]

        if not ("AutoWho" in fields and "AutoMethod" in fields and "AutoDate" in fields):
            print("No auto fields to update")
            return False

        autowho = os.environ['USERNAME'] # Who is logged in??
        automethod = "DIG"
        today = date.today()

        try:
            fields = ["AutoWho", "AutoMethod", "AutoDate"]
            with arcpy.da.UpdateCursor(self.fc, fields, where_clause="%s=%d" % (oidfield,fid)) as cursor:
                for row in cursor:
                    row[0] = autowho
                    row[1] = automethod
                    row[2] = today
                    cursor.updateRow(row)
        except Exception as e:
            print("Exception in update of %s: %s" % (fc, e))
            return False

        return True

if __name__ == "__main__":
    workspace = "C:\\GeoModel\\Clatsop\\Workfolder\\ORMap_Clatsop.gdb\\taxlots_fd"

    fc = "taxlot"
    arcpy.env.workspace = workspace

    u = AttrUpdate(fc)
    u.update_auto(32521)

    print("That's all.")
