import concurrent.futures
import time

NUMBERS = [
   2,  # prime
   1099726899285419,
   1570341764013157,  # prime
   1637027521802551,  # prime
   1880450821379411,  # prime
   1893530391196711,  # prime
   2447109360961063,  # prime
   3,  # prime
   2772290760589219,  # prime
   3033700317376073,  # prime
   4350190374376723,
   4350190491008389,  # prime
   4350190491008390,
   4350222956688319,
   2447120421950803,
   5,  # prime
]

def prime_factors(number):
   if number < 2:
      return False
   for i in range(2, int(number ** 0.5) + 1):
      if number % i == 0:
         return False
   return True

def simple_execution():
   bools = []
   for num in NUMBERS:
      bools.append(prime_factors(num))
   return bools

def threading_execut():
   with concurrent.futures.ThreadPoolExecutor() as executor_thread:
      executor_thread.map(prime_factors, NUMBERS)

def processing_execut():
   with concurrent.futures.ProcessPoolExecutor() as executor_proc:
      executor_proc.map(prime_factors, NUMBERS)

if __name__ == '__main__':
   print(simple_execution())
   start_time = time.time()
   processing_execut()
   print(time.time() - start_time)


# processing_execut()  5.09sec
# threading_execut()   17.74sec