# Ranked-Choice Voting System

This project implements a Ranked-Choice Voting (RCV) system in Python. Ranked-choice voting is an electoral system where voters rank candidates in order of preference instead of selecting only one candidate. If no candidate receives a majority of first-choice votes, the candidate with the fewest votes is eliminated and their votes are redistributed based on the next preference indicated on each ballot. This process continues until a candidate obtains a majority.

## Features
<ul>
  <li>Accepts ballots where voters rank candidates by preference
  <li>Automatically counts first-choice votes</li>
  <li>Eliminates the candidate with the fewest votes in each round</li>
  <li>Redistributes votes according to the next available preference</li>
  <li>Continues until a candidate achieves a majority</li>
</ul>

## How It Works
<ol>
  <li>Each voter submits a ballot ranking candidates.</li>
  <li>The system counts all first-choice votes.</li>
  <li>If a candidate has more than 50%, they win.</li>
  <li>If not, the candidate with the fewest votes is eliminated.</li>
  <li>Ballots for the eliminated candidate are reassigned to the next preferred candidate.</li>
  <li>Steps 2–5 repeat until a winner is determined.</li>
  <li>If there are multiple candidates with same status, all of them will be elected</li>
</ol>

## Example Ballot Format
`ballots = [
["Alice", "Bob", "Charlie"],
["Bob", "Charlie", "Alice"],
["Charlie", "Alice", "Bob"],
["Charlie", "Bob", "Alice"],
["Bob", "Alice", "Charlie"]
]
`
