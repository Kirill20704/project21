''' Переписаить упрощённую версию игры BlackJack с использованием рекурентных функций. Пользователь играет с программой. Побеждает тот, кто набрал сумму очков ближайшую к 21, но не превышающую её. Ввод 1 - 'взять карту, 0 - перестать брать карты, 2 после окончания партии - выйти из игры '''
def prob(list1, n=0, i=1):
	''' Упрощённый рассчёт вероятности для пртнятия решения программой +rec'''
	try:
		num = sum(f11or1(list1))
		n += list1.count(i)
		if ((21-num)*4-n)/(52 - len(list1)) > 0.5:
			return 1
		return prob(list1, n, i+1)
	except:
		return 0


from random import *
s = [ [i + j for i in ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A'] ] for j in '♤♡◇♧']
z = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, [11, 1]]
def ch(s, z):
	''' "Достать случайную карту из колоды" '''
	r1 = choice(s)
	r2 = choice(r1)
	ind = z[r1.index(r2)]
	return [s.index(r1), r2, ind]


def filt(a, b):
	''' Предотвращение повторений карт +rec'''
	y = a
	r = y[1]
	x = y[2]
	if r not in b:
		return [r,x]
	return filt(ch(s, z),b)


def f11or1(a, j=0, s=0):
	''' Туз начисляет либо 11 очков, либо 1. Эта функция определяет, какое значение выбрать +rec'''
	if a.count([11, 1]) == 0:
		return a
	else:
		c = a.count([11, 1])
		for i in range(c):
			a.remove([11, 1])
		s = sum(a)
		d = a
		if j == c:
			return d
		if s <= 10 and c == 1:
			s += 11
			d.append(11)
		else:
			s += 1
			d.append(1)
		return f11or1(a, j, s)


''' Переменные с индексом 1 относятся к игроку, с индексом 2 - к его сопернику (программе)' '''
p1 = 0
p2 = 0
while True:
	a = int(input())
	if a == 2:
		break
	t1 = ch(s, z)
	v = [t1[1]] # список использованных карт
	n1 = [t1[2]] # список общим количеством очков игрока
	print(v[0])
	t2 = ch(s, z)
	v.append(t2[1])
	v2 = [t2[1]] # список испооьзованных карт программы
	n2 = [t2[2]] # список с общим количеством очков программы
	b = 1
	while a != 0 or b != 0:
		if a != 0:
			a = int(input())
			if a == 0:
				continue
			t1 = filt(ch(s, z), v)
			v.append(t1[0])
			print(t1[0])
			n1.append(t1[1])
		if b != 0:
			t2 = filt(ch(s, z), v)
			v.append(t2[0])
			v2.append(t2[0])
			n2.append(t2[1])
			b = prob(f11or1(n2))
			n2 = f11or1(n2)
	print('Сумма:' , sum(f11or1(n1)), '|', v2, sum(n2))
	if sum(n2) < sum(f11or1(n1)) <= 21 or (sum(f11or1(n1)) <= 21 and sum(n2) > 21):
		print('Вы выйграли')
		p1 += 1
	elif sum(f11or1(n1)) == sum(n2) or (sum(f11or1(n1)) > 21and sum(n2) > 21):
		print('Ничья')
	else:
		print('Вы проиграли')
		p2 += 1
print('Игра окончена')
print('Счёт: [', p1, ':', p2, ']')
