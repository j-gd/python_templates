'''
Goal-oriented programming
* Provide answers to goals
* Help people learn Python

'''
import pandas as pd
import numpy as np
import warnings

from eda import eda

class GoalCoding():
    def __init__(self,
    visual_check=True,
    file_name_or_python_object=None,
    name_to_give_the_instance_object = None,
    nb_rows_to_read=-1, ):
        '''
        PARADIGM:
        A class that lets you code by goals and sub-goals selection via tabbing

        First you need to define the data to work on, either at creation or using the configure action

        Then, hit tab on your instance to explore the actions you can perform

        By default, the instance performs actions on the last object manipulated and saves it to the same, but you can specify other ones as arguments


        OPTIONAL INPUT (sent to your_instance.configure)
          visual_check: print a visual check of the result of actions that modify objects
          file_name_or_python_object: the initial data to process
          name_to_give_the_instance_object: the name of the initial data copied into this instance
          nb_rows_to_read (int): -1 reads everything
        '''
        self.eda = eda(self)
        self.subset_rows = SubsetRows(self)
        self.configure = Configure(self)
        self._visual_check = visual_check
        self.objects = Objects(self)

        if file_name_or_python_object != None:
            self.objects.add_object(file_name_or_python_object,
                                    name_to_give_the_instance_object,
                                    nb_rows_to_read)



class Configure():
    def __init__(self, goal):
        self._ = goal

    def set_visual_check(self, visual_check_length=3):
        '''
      visual_check_length: number of lines of the result to display
        -1: don't display anything
      '''
        self._._visual_check_length = visual_check_length


class Objects():
    ''' 
  Where all user objects are stored
  '''
    def __init__(self, goal):
        self._ = goal
        self._objs = {}

    def add_object(self, file_name_or_python_object, name_to_give_the_instance_object, nb_rows_to_read=-1):
        warnings.simplefilter('error', UserWarning)
        try:
            if file_name_or_python_object == None:
                print('Usage: GoalCoding(file_name_or_python_object)')
            elif isinstance(file_name_or_python_object, (pd.DataFrame,pd.Series)):
                if nb_rows_to_read < 1:
                    self.objs[name_to_give_the_instance_object] = file_name_or_python_object.copy()
                else:
                    self.objs[name_to_give_the_instance_object] = file_name_or_python_object[:nb_rows_to_read].copy()
            elif isinstance(file_name_or_python_object, str):
                if nb_rows_to_read < 1:
                    self.objs[name_to_give_the_instance_object] = pd.read_csv(file_name_or_python_object)
                else:
                    self.objs[name_to_give_the_instance_object] = pd.read_csv(file_name_or_python_object,
                                        nrows = nb_rows_to_read)
            else:
                print('Unsupported input type')
        except:
            raise

    def set_last_used(self, object_name):
      if not object_name in self._objs.keys():
        print("Error, the object {} is not in this instance's objects".format(object_name))
        return

      self._last_used = object_name



class SubsetRows():
    def __init__(self, goal):
        self._ = goal

    def meet_logical_criteria(self, condition_or_filter_for_samples_to_keep,
                              on_object='last_used', to_object='same'):
        if on_object == 'last_used':
            on_object = self._.df

        if isinstance(on_object, pd.DataFrame) or isinstance(on_object, pd.DataFrame) \
          or isinstance(on_object, np.array):
            print('df_or_series_or_np_array[condition_or_filter_for_samples_to_keep]')

            if to_object == 'same':
                on_object = on_object[condition_or_filter_for_samples_to_keep]
            else:
                self._.objects[to_object] = on_object[condition_or_filter_for_samples_to_keep]

            if self._._visual_check_length > 0:
                print(res[:self._._visual_check_length])
        else:
            print('Unsupported object type:', type(on_object))
            print('Supported types are Pandas DataFrame, Series or Numpy array')


    def drop_duplicates(self,
                              object_to_filter='last_used',save='same'):
        '''
        object_to_filter: 
            'last_used' (default): use on the last object processed by this GoalCode instance
            or specify a different object to process, e.g. object_to_filter=df2

        save: 
            'inplace' (default) saves in place
            'new' to save as a new object of same type
            'no' don't save the result

        To turn debug-print on/off for the result of the operation, call manage_goal_coding.set_debug()
        '''
        if object_to_filter == 'last_used':
            object_to_filter = self._.df

        if isinstance(object_to_filter, pd.DataFrame) or isinstance(
                object_to_filter, pd.DataFrame):
            print('df_or_series.drop_duplicates()')
            return object_to_filter.drop_duplicates(inplace)
        else:
            print('Unsupported object type:', type(object_to_filter))
            print(
                'Currently supported types are Pandas DataFrame or Series')
