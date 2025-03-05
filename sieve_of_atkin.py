import numpy as np
import time

class Primer:
	# Sieve of Atkin algo
	@staticmethod
	def sieve(limit):
		#start time
		start_time = time.time()

		numbers = np.arange(2, limit + 1).tolist()
		primes = ['🟦'] * (limit + 1)
		primes[0], primes[1] = '🟦', '🟦'

		for test_number in range(2, 7 + 1):
			for index in range(1, len(numbers)):
				if numbers[index] % test_number == 0 and numbers[index] != test_number:
					primes[index] = '🟥'

		# calculation time
		completed_tast_time.append(time.time() - start_time)
		return primes

	# CHATGPT answer 
	@staticmethod
	def brute(limit):
		#start time
		start_time = time.time()

		primes = []
		for number in range(2, limit + 1):
			# if current numer is prime
			is_prime = all(number % i != 0 for i in range(2, int(number ** 0.5) + 1))
			if is_prime:
				primes.append('🟦')
			else:
				primes.append('🟥')

		# calculation time
		completed_tast_time.append(time.time() - start_time)
		return primes

def main():
	global completed_tast_time
	completed_tast_time = []
	limit = 1000000

	# calculations
	Primer.sieve(limit)
	Primer.brute(limit)

	print(f'\nnumbers {limit}')
	print(f'''
			Sieve of Atkin
			--- {completed_tast_time[0]} seconds ---
	''')

	print(f'''
			Normal Primer
			--- {completed_tast_time[1]} seconds ---
	''')

	print(f'Sieve is {round(completed_tast_time[1] / completed_tast_time[0], 2)}x faster\n')

if __name__ == '__main__':
	main()