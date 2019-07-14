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
    def __init__(self, file_name_or_pd_dataframe, nb_rows_to_read=-1, visual_check=True):
        '''
        PARADIGM:
        A class that lets you code by goals and sub-goals selection via tabbing

        First you need to define the data to work on, either at creation or using the configure action

        Then, hit tab on your instance to explore the actions you can perform

        By default, the instance performs actions on the last object manipulated and saves it to the same, but you can specify other ones as arguments


        OPTIONAL INPUT (sent to your_instance.configure)
          file_name_or_pd_dataframe: the data to process
          nb_rows_to_read (int): -1 reads everything
          visual_check: print a visual check of the result of actions that modify objects
        '''

        warnings.simplefilter('error', UserWarning)
        try:
            if file_name_or_pd_dataframe == None:
                print('Usage: GoalProgramming(file_name_or_pd_dataframe)')
            elif isinstance(file_name_or_pd_dataframe, (pd.DataFrame,pd.Series)):
                if nb_rows_to_read < 1:
                    self.df = file_name_or_pd_dataframe
                else:
                    self.df = file_name_or_pd_dataframe[:nb_rows_to_read]
            elif isinstance(file_name_or_pd_dataframe, str):
                if nb_rows_to_read < 1:
                    self.df = pd.read_csv(file_name_or_pd_dataframe)
                else:
                    self.df = pd.read_csv(file_name_or_pd_dataframe,
                                        nrows = nb_rows_to_read)
            else:
                print('Unsupported input type')
        except:
            raise
        self.eda = eda(self)
        self.subset_rows = SubsetRows(self)
        self.configure = Configure(self)
        self._visual_check = visual_check
        self.objects = Objects(self)


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

            if to_object='same':
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
