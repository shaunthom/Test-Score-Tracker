with open(filename) as file:
  
  high_name = 'nickname'
  low_name='random'
  high_score = 1
  low_score = 98
  students = {}
  
  for line in file:
  
      parts=line.split(',')
      name = parts[0]
  
      scores = [int(score) for score in parts[1:]]
      students[name] = scores
      average_score = sum(scores) / len(scores)
      if average_score > high_score:
          high_score = average_score
          high_name = name
      if average_score < low_score:
          low_score = average_score
          low_name = name
  HIGH = high_name
  LOW = low_name
  #alternate algorithms can also be developed
  
  return (HIGH, round(high_score,2) , LOW, round(low_score,2))
