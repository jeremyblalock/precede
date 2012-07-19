import os

class Datastore(object):
    def __init__(self, filename):
        if not os.isdir(filename) and not os.path.exists:
            try:
                os.mkdir(os.path.expanduser(filename))
            except:
                raise Exception("Could not create directory '%s'" % os.path.expanduser('filename'))
            try:
                datafile = open('%s/data' % filename, 'w')
                indexfile = open('%s/index' % filename, 'w')
            except:
                raise Exception("Could not create database files")

        elif os.path.exists:
            raise Exception('Specified filename is not a directory')
        try:
            self.datafile = open('%s/data' % filename, 'r+')
            self.index = open('%s/index' % filename, 'r+')
        except:
            raise Exception('Database files appear to be corrupted')
