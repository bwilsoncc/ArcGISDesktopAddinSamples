from __future__ import print_function
import arcpy
import pythonaddins
#from update import AttrUpdate

class ExtensionTest(object):
    """Implementation for PythonAddin_addin.extTest (Extension)"""

    # Refer to http://desktop.arcgis.com/en/arcmap/latest/analyze/python-addins/extension-class.htm

    count = 0

    def say_what(self):
        for k in self.__dict__:
            val = self.__dict__[k]
            print("   ", k, " => ", val)
    
    def __init__(self):
        # For performance considerations, please remove all unused methods in this class.
        self.enabled = True
        print("ExtensionTest.init(self)")
        self.say_what()
        
    def startup(self):
        print("%d startup(self)" % self.count)
        self.count += 1
        self.say_what()
        
    def activeViewChanged(self):
        print("%d activeViewChanged(self)" % self.count)
        self.count += 1
        self.say_what()
        
    def mapsChanged(self):
        print("%d mapsChanged(self)" % self.count)
        self.count += 1
        self.say_what()
        
    def newDocument(self):
        print("%d newDocument(self)" % self.count)
        self.count += 1
        self.say_what()
        
    def openDocument(self):
        print("%d openDocument(self)" % self.count)
        self.count += 1
        self.say_what()
        
    def beforeCloseDocument(self):
        print("%d beforeCloseDocument(self)" % self.count)
        self.count += 1
        self.say_what()
        
    def closeDocument(self):
        print("%d closeDocument(self)" % self.count)
        self.count += 1
        self.say_what()
        
    def beforePageIndexExtentChange(self, old_id):
        print("%d beforePageIndexExtentChange(self, old_id)" % self.count, old_id)
        self.count += 1
        self.say_what()
        
    def pageIndexExtentChanged(self, new_id):
        print("%d pageIndexExtentChanged(self, new_id)" % self.count, new_id)
        self.count += 1
        self.say_what()

    def contentsChanged(self):
        print("%d contentsChanged(self)" % self.count)
        self.count += 1
        self.say_what()

    def spatialReferenceChanged(self):
        print("%d spatialReferenceChanged(self)" % self.count)
        self.count += 1
        self.say_what()

    def itemAdded(self, new_item):
        print("%d itemAdded(self, new_item)" % self.count, new_item)
        self.count += 1
        self.say_what()

    def itemDeleted(self, deleted_item):
        print("%d itemDeleted(self, deleted_item)" % self.count, deleted_item)
        self.count += 1
        self.say_what()

    def itemReordered(self, reordered_item, new_index):
        print("%d itemReordered(self, reordered_item, new_index)" % self.count, new_index)
        self.count += 1
        self.say_what()

    def onEditorSelectionChanged(self):
        print("%d onEditorSelectionChanged(self)" % self.count)
        self.count += 1
        self.say_what()

    def onCurrentLayerChanged(self):
        print("%d onCurrentLayerChanged(self)" % self.count)
        self.count += 1
        self.say_what()

    def onCurrentTaskChanged(self):
        print("%d onCurrentTaskChanged(self)" % self.count)
        self.count += 1
        self.say_what()

    def onStartEditing(self):
        print("%d onStartEditing(self)" % self.count)
        self.count += 1
        self.say_what()

    def onStopEditing(self, save_changes):
        print("%d onStopEditing(self, save_changes)" % self.count, save_changes)
        self.count += 1
        self.say_what()

    def onStartOperation(self):
        print("%d onStartOperation(self)" % self.count)
        self.count += 1
        self.say_what()

    def beforeStopOperation(self):
        print("%d beforeStopOperation(self)" % self.count)
        self.count += 1
        self.say_what()

    def onStopOperation(self):
        print("%d onStopOperation(self)" % self.count)
        self.count += 1
        #self.say_what()
        desc = self.currentFeature
        selections = self.editSelection
        workspace = self.editWorkspace
        print("Workspace ", workspace)
        print("Selected ", selections)
        print("currentLayer", self.currentLayer)
        obj = pythonaddins.GetSelectedTOCLayerOrDataFrame()
        print("current thing", obj)


    def onSaveEdits(self):
        print("%d onSaveEdits(self)" % self.count)
        self.count += 1
        self.say_what()

    def onChangeFeature(self):
        print("%d onChangeFeature(self)" % self.count)
        self.count += 1
        self.say_what()

    def onCreateFeature(self):
        print("%d onCreateFeature(self)" % self.count)
        self.count += 1
        self.say_what()

    def onDeleteFeature(self):
        print("%d onDeleteFeature(self)" % self.count)
        self.count += 1
        self.say_what()

    def onUndo(self):
        print("%d onUndo(self)" % self.count)
        self.count += 1
        self.say_what()

    def onRedo(self):
        print("%d onRedo(self)" % self.count)
        self.count += 1
        self.say_what()


class TestButtonClass(object):
    """Implementation for PythonAddin_addin.button (Button)"""

    count = 0
    
    def say_what(self):
        for property, value in vars(TestButtonClass).iteritems():
            print("   ", property, ": ", value)
        for k in self.__dict__:
            val = self.__dict__[k]
            print("  k=", k, " => ", val)
    
    def __init__(self):
        self.checked = False
        print("TestButton init")
        self.say_what()
        
    def onClick(self):
        self.checked = not self.checked
        print("%d TestButton click; checked =" % self.count, self.checked)
        self.say_what()
        self.count += 1
        pass
