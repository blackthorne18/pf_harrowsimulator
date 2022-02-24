# Harrow Simulator

Harrow is the Pathfinder version of Tarrot cards. This simulators, provides a randomly shuffled spread of Tarrot cards based on the card category.<br>

## What is Harrow?
The Harrow is a method of divination widely used by many Varisian fortune-tellers using a Harrow deck and possibly the harrowing spell. By these means, the reader is said to be able to receive small bits of information about what has occurred, what is happening, and what will come to pass in the future. The system uses a deck of 54 cards with six suites representing different abilities and a card referencing each of the nine alignments (LE to CG) for each suite.<br>
A card is chosen at random from the suite corresponding to the question that the client wants answered. Then the cards are rearranged randomly into a nine by nine grid from which the harrower makes the reading.

## Why did I build this?
I was playing a Pathfinder game where my character was a Psychic and a Harrower. I needed an easy way to simulate the harrow deck and reading online since I didn't have the actual cards and we played online anyway. There weren't many harrow simulators online, none that I preferred and so I decided to make one myself.

## Features
First, you must select the corresponding ability that represents the question asked by the client. Then, the website simulates the nine by nine spread of shuffled harrow cards with an indiciation for the harrower as to the kind of match.<br>
By toggling the view, you can show/hide text indicating what each card represents in and off itself (for showing to the client vs for your own view). You can also copy a client-friendly ASCII version of the nine by nine spread that you can share to the client.<br>
Have the client roll 2d6. Halve the result of each die and this gives the coordinates on the nine by nine for which card is the 'chosen' card. It's easier this way since we're doing this online and because the first chosen card is selected at random anyway.

## [Link to website hosted on Heroku](harrowsimulator.herokuapp.com)

