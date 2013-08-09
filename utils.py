import sqlite3

def feature_names():
  return ["pixel%s" % (i,) for i in xrange(784)]

def values(feature_name):
  conn = sqlite3.connect("data/data.sqlite")
  cur = conn.cursor()
  result = cur.execute("SELECT DISTINCT %s from train" % feature_name)
  return cur

def is_homogenous(values):
  return len(set(values)) == 1

def non_homogenous_feature_names():
  return [x for x in feature_names() if not is_homogenous(values(x))]

