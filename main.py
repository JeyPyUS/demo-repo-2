for ix,tag in enumerate(nodes):
  row = dict(list(map(simple_dict, tag)))
  s_row = pd.Series(data = row).to_frame().T
  output.append(s_row)
