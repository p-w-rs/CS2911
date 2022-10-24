# Overview
In this lab, you will create and brute-force attack 16-bit RSA encryption. Before you can play out these scenarios, you will need code to create and use a public & private key.

Download and finish the file: **rsa.py**

# Requirments

Implement the three functions: create_keys, apply_key, break_key

For help on generating prime numbers see **prime_generator.py**

You can also use [this article](https://en.wikipedia.org/wiki/RSA_(cryptosystem)) if you forget the RSA steps

Feel free to look up how to perform these steps in python: such as totient functions, coprimaility, and modular inverses

# Reflection Questions
## Question 1: RSA Security
In this lab, Trudy is able to find the private key from the public key. Why is this not a problem for RSA in practice?

## Question 2: Critical Step(s)
When creating a key, Bob follows certain steps. Trudy follows other steps to break a key. What is the difference between Bob’s steps and Trudy’s so that Bob is able to run his steps on large numbers, but Trudy cannot run her steps on large numbers?