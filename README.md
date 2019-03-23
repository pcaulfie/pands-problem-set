# Problem Set 2019

This document contains a brief description of solutions for Problem Set 2019 for Programming and Scripting. There are ten solutions, one for each problem in the problem set.

## Getting Started

I have created a GitHub Repository where you can access my project, its files, and all the versions of its files that Git saves. See link https://github.com/pcaulfie/pands-problem-set

### Problem 1. Write a program that asks the user to input any positive integer and outputs the sum of all numbers between one and that number.
```
Example
$ python sumupto.py
Please enter a positive integer: 10
55
```
And repeat
```
Solution : https://github.com/pcaulfie/pands-problem-set/blob/master/sumupto.py
```

### Problem 2. Write a program that outputs whether or not today is a day that begins with the letter T. 

```
An example of running this program on a Thursday is as follows.
$ python begins-with-t.py
Yes - today begins with a T.
An example of running it on a Wednesday is as follows.
$ python begins-with-t.py
No - today does not begin with a T.
```

And repeat

```
https://github.com/pcaulfie/pands-problem-set/blob/master/begins-with-t.py
```

End with an example of getting some data out of the system or using it for a little demo

### Problem 3. Write a program that prints all numbers between 1,000 and 10,000 that are divisible by 6 but not 12.

```
$ python divisors.py
1002
1014
1026
etc
9990
```

And repeat

```
https://github.com/pcaulfie/pands-problem-set/blob/master/divisors.py
```

End with an example of getting some data out of the system or using it for a little demo

### Problem 4. Write a program that asks the user to input any positive integer and outputs the successive values of the following calculation. At each step calculate the next value by taking the current value and, if it is even, divide it by two, but if it is odd, multiply it by three and add one. Have the program end if the current value is one.

```
$ python collatz.py
Please enter a positive integer: 10
10 5 16 8 4 2 1
```

And repeat

```
https://github.com/pcaulfie/pands-problem-set/blob/master/collatz.py
```

End with an example of getting some data out of the system or using it for a little demo

### Problem 5. Write a program that asks the user to input a positive integer and tells the user whether or not the number is a prime.

```
$ python primes.py
Please enter a positive integer: 19
That is a prime.
```

And repeat

```
https://github.com/pcaulfie/pands-problem-set/blob/master/primes.py
```

End with an example of getting some data out of the system or using it for a little demo

### Problem 6. Write a program that takes a user input string and outputs every second word.

```
$ python secondstring.py
Please enter a sentence: The quick brown fox jumps over the lazy dog.
The brown jumps the dog
```

And repeat

```
https://github.com/pcaulfie/pands-problem-set/blob/master/secondstring.py
```

End with an example of getting some data out of the system or using it for a little demo

### Problem 7. Write a program that that takes a positive floating point number as input and outputs an approximation of its square root.

```
$ python squareroot.py
Please enter a positive number: 14.5
The square root of 14.5 is approx. 3.8.
```

And repeat

```
https://github.com/pcaulfie/pands-problem-set/blob/master/squareroot.py
```

End with an example of getting some data out of the system or using it for a little demo

### Problem 8. Write a program that outputs today’s date and time in the format “Monday, January 10th 2019 at 1:15pm”.

```
$ python datetime.py
Monday, January 10th 2019 at 1:15pm
```

And repeat

```
https://github.com/pcaulfie/pands-problem-set/blob/master/todaysdatetime.py
```

End with an example of getting some data out of the system or using it for a little demo

### Problem 9. Write a program that reads in a text file and outputs every second line. The program should take the filename from an argument on the command line.

```
$ python second.py moby-dick.txt
Title: Moby Dick; or The Whale
CHAPTER 1
Call me Ishmael. Some years ago--never mind how long
particular to interest me on shore, I thought I would sail about a
...
```

And repeat

```
https://github.com/pcaulfie/pands-problem-set/blob/master/second.py
```

End with an example of getting some data out of the system or using it for a little demo

### Problem 10. Write a program that displays a plot of the functions x, x2 and 2x in the range [0, 4].

```

```

And repeat

```
https://github.com/pcaulfie/pands-problem-set/blob/master/displayplot.py
```

End with an example of getting some data out of the system or using it for a little demo

## Deployment

Add additional notes about how to deploy this on a live system

## Built With

* [Dropwizard](http://www.dropwizard.io/1.0.2/docs/) - The web framework used
* [Maven](https://maven.apache.org/) - Dependency Management
* [ROME](https://rometools.github.io/rome/) - Used to generate RSS Feeds

## Contributing

Please read [CONTRIBUTING.md](https://gist.github.com/PurpleBooth/b24679402957c63ec426) for details on our code of conduct, and the process for submitting pull requests to us.

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/your/project/tags). 

## Authors

* **Billie Thompson** - *Initial work* - [PurpleBooth](https://github.com/PurpleBooth)

See also the list of [contributors](https://github.com/your/project/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Hat tip to anyone whose code was used
* Inspiration
* etc
