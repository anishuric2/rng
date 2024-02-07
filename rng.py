class MiddleSquare:
    """
    MiddleSquare Class

    This class represents a simple random number generator using the middle-square method.

    Attributes:
    - seed (int): The initial seed value.
    - __state (dict): Dictionary representing the current state of the generator.
      - 'val' (int): Current value in the sequence.
      - 'ndigits' (int): Number of digits in the seed.
    - seen_numbers (set): Set to keep track of seen numbers in the sequence.
    """

    def __init__(self, seed: int):
        """
        Initializes the MiddleSquare object with the specified seed.
        Parameters:
        - seed (int): The initial seed value.
        Raises:
        - TypeError: If the provided seed is not an integer.
        - ValueError: If the length of the seed is not even.
        """
        if not isinstance(seed, int):
            raise TypeError("Seed must be an integer")

        # Convert the seed to a string for processing
        str_seed = str(seed)

        # Check if the length of the seed is even
        if len(str_seed) % 2 != 0:
            raise ValueError("Seed must have an even number of digits")

        # Convert the seed back to an integer and store it as an attribute
        self.seed = int(str_seed)

        # Initialize the internal state dictionary with the seed and its number of digits
        self.__state = {"val": self.seed, "ndigits": len(str(self.seed))}
        # Initialize a set to keep track of seen numbers
        self.seen_numbers = set()



    def __iter__(self):
        """
        Makes the instance iterable.
        Returns:
        - MiddleSquare: The iterator object (self).
        """
        return self

    def __next__(self):
        """
        Generates the next value in the middle-square sequence.
        Returns:
        - int: The next value in the sequence.
        Raises:
        - StopIteration: When the sequence starts repeating.
        """
        # Retrieve the current state from the internal dictionary
        state = self.__state

        # Square the current value of the state
        state["val"] = state["val"] ** 2

        # Convert the squared value to a string and pad with zeros
        str_val = str(state["val"]).zfill(2 * state["ndigits"])

        # Extract the middle part of the string
        state["val"] = int(str_val[(state["ndigits"] // 2): (3 * state["ndigits"] // 2)])

        # Check if the new value has been seen before, then stop
        if state["val"] in self.seen_numbers:
            raise StopIteration()

        # Update the set of seen numbers
        self.seen_numbers.add(state["val"])
        return state["val"]

    def get_state(self):
        """
        Returns a copy of the internal state dictionary to prevent any errors.
        Returns:
        - dict: Dictionary containing 'val' and 'ndigits' keys with their respective values.
        """
        return self.__state.copy()

    def set_state(self, state):
        """
        Sets the state of the generator based on the provided dictionary.
        Parameters:
        - state (dict): Dictionary containing 'val' and 'ndigits' keys.
        Raises:
        - ValueError: If the provided dictionary is invalid.
        """
        if "ndigits" in state and "val" in state:
            self.__state = state
        else:
            raise ValueError("Invalid dictionary")



class LinearCongruential:
    """
    LinearCongruential Class
    This class represents a linear congruential generator.
    Attributes:
    - seed (int): The initial seed value.
    - __a (int): Multiplier value in the linear congruential formula.
    - __c (int): Increment value in the linear congruential formula.
    - __m (int): Modulus value in the linear congruential formula.
    - __value (int): Current value in the sequence.
    - __state (dict): Dictionary representing the current state of the generator.
      - 'val' (int): Current value in the sequence.
      - 'a' (int): Multiplier value.
      - 'c' (int): Increment value.
      - 'm' (int): Modulus value.
    - __seen_numbers (set): Set to keep track of seen numbers in the sequence.
    """

    def __init__(self, seed: int, a: int, c: int, m: int):
        """
        Initializes the LinearCongruential object with the specified parameters.
        Parameters:
        - seed (int): The initial seed value.
        - a (int): Multiplier value in the linear congruential formula.
        - c (int): Increment value in the linear congruential formula.
        - m (int): Modulus value in the linear congruential formula.
        """
        self.seed = seed
        self.__a = a
        self.__c = c
        self.__m = m
        self.__value = seed
        self.__state = {"val": seed, "a": a, "c": c, "m": m}
        self.__seen_numbers = set()

    def __iter__(self):
        """
        Makes the instance iterable.
        Returns:
        - LinearCongruential: The iterator object (self).
        """
        return self

    def __next__(self):
        """
        Generates the next value in the linear congruential sequence.
        Returns:
        - int: The next value in the sequence.
        Raises:
        - StopIteration: When the sequence starts repeating.
        """
        if self.__value in self.__seen_numbers:
            raise StopIteration

        self.__seen_numbers.add(self.__value)
        self.__value = (self.__a * self.__value + self.__c) % self.__m
        return self.__value

    def get_state(self):
        """
        Returns a dictionary representing the current state of the generator.
        Returns:
        - dict: Dictionary containing 'val', 'a', 'c', and 'm' keys with their respective values.
        """
        return {"val": self.__value, "a": self.__a, "c": self.__c, "m": self.__m}

    def set_state(self, state):
        """
        Sets the state of the generator based on the provided dictionary.
        Parameters:
        - state (dict): Dictionary containing 'val', 'a', 'c', and 'm' keys.
        Raises:
        - ValueError: If the provided dictionary is invalid.
        """
        self.__a = state['a']
        self.__c = state['c']
        self.__m = state['m']
        self.__value = state['val']
        self.__seen_numbers = set()



class LaggedFibonacci:
    """
    LaggedFibonacci Class
    This class represents a Lagged Fibonacci random number generator.
    Attributes:
    - __state (dict): Dictionary representing the current state of the generator.
      - 'val' (list): List containing the current values in the sequence.
      - 'j' (int): Integer-valued j.
      - 'k' (int): Integer-valued k.
      - 'm' (int): Integer-valued modulus.
    - __value (list): Initial seed values to check for the end of the sequence.
    """

    def __init__(self, seed: list[int], j: int, k: int, m: int):
        """
        Initializes the LaggedFibonacci object with the specified parameters.
        Parameters:
        - seed (list[int]): The initial seed values.
        - j (int): Integer-valued j.
        - k (int): Integer-valued k.
        - m (int): Integer-valued modulus.
        Raises:
        - TypeError: If seed is not a list of integers or if any element in the seed is not an integer.
        - ValueError: If m is not an integer or if j, k, or seed length have invalid values.
        """
        if not isinstance(seed, list):
            raise TypeError("Seed must be a list of integers.")

        for item in seed:
            if not isinstance(item, int):
                raise TypeError("All elements in the seed must be integers.")

        if not isinstance(m, int):
            raise ValueError("Param M must be an integer")

        # Validate the value of j and k so that k is less than the length of the seed and j is greater than 0 and less than k
        if not (0 < j < k <= len(seed)):
            raise ValueError("Invalid values for j, k, or seed length.")

        # Initialize the internal state dictionary with the seed, j, k, and m
        self.__state = {"val": seed, "j": j, "k": k, "m": m}
        # Copy the initial seed to check for the end of the sequence
        self.__value = seed.copy()

    def __iter__(self):
        """
        Makes the instance iterable.
        Returns:
        - LaggedFibonacci: The iterator object (self).
        """
        return self

    def __next__(self):
        """
        Generates the next number in the Lagged Fibonacci sequence.
        Returns:
        - int: The next number in the sequence.
        Raises:
        - StopIteration: When the sequence returns to the initial seed.
        """
        # Get the current state values
        state = self.__state["val"]
        j = self.__state["j"]
        k = self.__state["k"]
        m = self.__state["m"]

        # Calculate the next number
        next_number = (state[-k] + state[-j]) % m

        # Update the state by appending the next number and removing the first element
        state.append(next_number)
        state.pop(0)

        # Check if we've returned to the initial seed, then stop the iteration
        if state == self.__value:
            raise StopIteration()

        return next_number

    def get_state(self):
        """
        Returns the current state of the generator.
        Returns:
        - dict: Dictionary containing 'val', 'j', 'k', and 'm' keys with their respective values.
        """
        return self.__state

    def set_state(self, state):
        """
        Sets the state of the generator based on the provided dictionary.
        Parameters:
        - state (dict): Dictionary containing 'val', 'j', 'k', and 'm' keys.
        Raises:
        - ValueError: If the provided dictionary is invalid.
        """
        if not isinstance(state, dict):
            raise ValueError("Invalid state format.")
        self.__state = state



class Acorn:
   """
   Acorn Class
   This class represents an Acorn random number generator.
   Attributes:
   - state (dict): Dictionary representing the current state of the generator.
     - 'vals' (list): List containing the current values in the sequence.
     - 'M' (int): Integer-valued modulus.
   - seed (list): Initial seed values to check for the end of the sequence.
   - seen_numbers (list): List to keep track of seen number tuples in the sequence.
   """


   def __init__(self, seed: list[int], M: int):
       """

       Initializes the Acorn object with the specified parameters.
       Parameters:
       - seed (list[int]): The initial seed values.
       - M (int): Integer-valued modulus.
       Raises:
       - TypeError: If seed is not a list or if any element in the seed is not an integer.
       - ValueError: If M is not an integer or if the first element of the seed is greater than or equal to M.
       """
       if not isinstance(seed, list):
           raise TypeError("Seed must be a list")


       for i in seed:
           if not isinstance(i, int):
               raise TypeError("Seed must be a list of integers")

       if not isinstance(M, int):
           raise ValueError("M must be an integer.")

       if seed[0] >= M:
           raise ValueError("First element of seed must be less than M")

# Initialize the internal state dictionary with the seed and M
       self.state = {"vals": seed, "M": M}
# Copy the initial seed to check for the end of the sequence
       self.seed = seed
# Store the seen number tuples in a list
       self.seen_numbers = [tuple(seed)]


   def __iter__(self):
       """
       Makes the instance iterable.
       Returns:
       - Acorn: The iterator object (self).
       """
       return self


   def __next__(self):
       """
       Generates the next set of values in the Acorn sequence.
       Returns:
       - list: The next set of values in the sequence.
       Raises:
       - StopIteration: When the sequence returns to the initial seed.
       """
       state = self.state
       new_vals = [state["vals"][0]]


       for i in range(1, len(state["vals"])):
           new_vals.append((new_vals[i - 1] + state["vals"][i]) % self.state["M"])

# Check if the new set of values matches the initial seed, then stop the iteration
       if new_vals == self.seed:
           raise StopIteration()

# Update the state with the new set of values
       state["vals"] = new_vals
       return new_vals


   def get_state(self):
       """
       Returns the current state of the generator.
       Returns:
       - dict: Dictionary containing 'vals' and 'M' keys with their respective values.
       """
       return self.state


   def set_state(self, state):
       """
       Sets the state of the generator based on the provided dictionary.
       Parameters:
       - state (dict): Dictionary containing 'vals' and 'M' keys.
       Raises:
       - ValueError: If the provided dictionary is invalid.
       """
       if "vals" in state and "M" in state:
           self.state["vals"] = state["vals"]
           self.state["M"] = state["M"]
       else:
           raise ValueError("Invalid state format. Must include 'vals' and 'M'.")

class Analyzer:
  """
  Analyzer Class
  This class provides analysis capabilities for a given random number generator.
  Attributes:
  - rand_num_gen: The random number generator to be analyzed.
  - max: The maximum value observed during analysis.
  - min: The minimum value observed during analysis.
  - average: The average value observed during analysis.
  - period: The period of the random number generator.
  - bit_freqs: List containing the frequencies of each bit position in the binary representation of observed numbers.
  """

  def __init__(self, rand_num_gen):
      """
      Initializes the Analyzer object with the specified random number generator.
      Parameters:
      - rand_num_gen: The random number generator to be analyzed.
      """
      self.rand_num_gen = rand_num_gen
      self.max = None
      self.min = None
      self.average = 0
      self.period = 0
      self.bit_freqs = []

  def analyze(self, max_nums=1e5):
      """
      Analyzes the output of the random number generator.
      Parameters:
      - max_nums (float): Maximum number of random values to analyze. Default is 1e10.
      Returns:
      None
      """
      total = 0
      count = 0
      seen_numbers = set()

      for num_list in self.rand_num_gen:
          if count >= max_nums:
              break

          # Check if the output is a single value or a list
          if isinstance(num_list, list):
              numbers = num_list
          else:
              numbers = [num_list]

          for num in numbers:
              # Update min and max
              if self.min is None or num < self.min:
                  self.min = num
              if self.max is None or num > self.max:
                  self.max = num


              # Update total
              total += num

              # Count the number of bits needed to write the largest value in binary
              bit_length = len(bin(self.max)) - 2
              if len(self.bit_freqs) < bit_length:
                  self.bit_freqs.extend([0] * (bit_length - len(self.bit_freqs)))

              # Update bit frequencies for the binary of the current number
              for i in range(bit_length):
                  if num & (1 << i): #Shift left
                      self.bit_freqs[i] += 1


              # Track seen numbers for period calculation
              seen_numbers.add(num)

              count += 1


      # Calculate average after the loop
      if count > 0:
          self.average = total / count
      else:
          self.average = 0

      # Calculate period
      if isinstance(self.rand_num_gen, Acorn):
          self.period = len(seen_numbers)
      else:
          self.period = count


#MIDDLE SQUARE
ms_seed = 45725946
ms = MiddleSquare(ms_seed)
ms_analyze = Analyzer(ms)

# Analyze the random number generators
ms_analyze.analyze()
print(f'MAX:  {ms_analyze.max}')
print(f'MIN:  {ms_analyze.min}')
print(f'Average:  {ms_analyze.average}')
print(f'Period:  {ms_analyze.period}')
print(f'Bit Frequency:  {ms_analyze.bit_freqs}')

# Analyze the random number generators

'''
    LinearCongruential
'''

lcg_seed = 36
lcg_a = 455
lcg_c = 9126
lcg_m = 879

lcg = LinearCongruential(lcg_seed, lcg_a, lcg_c, lcg_m)
lcg_analyze = Analyzer(lcg)

lcg_analyze.analyze()
print(f'MAX:  {lcg_analyze.max}')
print(f'MIN:  {lcg_analyze.min}')
print(f'Average:  {lcg_analyze.average}')
print(f'Period:  {lcg_analyze.period}')
print(f'Bit Frequency:  {lcg_analyze.bit_freqs}')


'''
    Laggedfibonacci
'''
lf_seed = [1,2,3,4,6,1,4]
lf_j = 1
lf_k = 6
lf_m = 365

lf = LaggedFibonacci(lf_seed, lf_j, lf_k, lf_m)
lf_analyze = Analyzer(lf)

lf_analyze.analyze()
print(f'MAX:  {lf_analyze.max}')
print(f'MIN:  {lf_analyze.min}')
print(f'Average:  {lf_analyze.average}')
print(f'Period:  {lf_analyze.period}')
print(f'Bit Frequency:  {lf_analyze.bit_freqs}')

'''
Acorn
'''

ac_seed = [1,5,6,4,4,5,8,9,4]
ac_M = 12356


ac_acorn = Acorn(ac_seed, ac_M)
ac_analyze = Analyzer(ac_acorn)

ac_analyze.analyze()
print(f'MAX:  {ac_analyze.max}')
print(f'MIN:  {ac_analyze.min}')
print(f'Average:  {ac_analyze.average}')
print(f'Period:  {ac_analyze.period}')
print(f'Bit Frequency:  {ac_analyze.bit_freqs}')



