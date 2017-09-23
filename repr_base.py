from datetime import date

class ReprBase(object):
    '''Generic base class for consistent repr function'''
    dollar_attrs = []
    def __repr__(self):
        repr_list = []
        for k, v in self.__dict__.items():
            if k in self.dollar_attrs:
                v = '${:.2f}'.format(v)
            elif isinstance(v, date):
                v = '{:%m/%d/%Y}'.format(v)
            k = k.replace('_', ' ')
            repr_list.append('{}: {}'.format(k, v))
        return '\n'.join(sorted(repr_list, key=self._sort))
        
    @staticmethod
    def _sort(key):
        key = key.split(':')[0].lower()
        sort_keys = ['id', 'name']
        try:
            return sort_keys.index(key)
        except ValueError:
            return float('inf')
