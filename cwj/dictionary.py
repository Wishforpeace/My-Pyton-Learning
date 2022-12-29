score = {'Chinese': 88, 'Math': 91, 'English': 92, 'Physics': 86, 'Chemistry': 82}
append = {'Biology': 85}
score.update(append)

score['Math'] = 95
del score['Physics']

for i, j in score.items():
    print('Subject:%-10s   Score:%d' % (i, j))
