l'''
Write a class called User that is used to calculate the amount that a user will
progress through a ranking system similar to the one Codewars uses.

Business Rules:
A user starts at rank -8 and can progress all the way to 8.
There is no 0 (zero) rank. The next rank after -1 is 1.
Users will complete activities. These activities also have ranks.
Each time the user completes a ranked activity the users rank progress is
updated based off of the activity's rank
The progress earned from the completed activity is relative to
what the user's current rank is compared to the rank of the activity
A user's rank progress starts off at zero, each time the progress
reaches 100 the user's rank is upgraded to the next level

Any remaining progress earned while in the previous rank will be
applied towards the next rank's progress (we don't throw any progress away).
The exception is if there is no other rank left to progress towards
(Once you reach rank 8 there is no more progression).
A user cannot progress beyond rank 8.
The only acceptable range of rank values is
-8,-7,-6,-5,-4,-3,-2,-1,1,2,3,4,5,6,7,8. Any other value should raise an error.
The progress is scored like so:

Completing an activity that is ranked the same as that of the user's will be
worth 3 points
Completing an activity that is ranked one ranking lower than the user's will be
worth 1 point
Any activities completed that are ranking 2 levels or more lower than the
user's ranking will be ignored

Completing an activity ranked higher than the current user's rank will
accelerate the rank progression. The greater the difference between
rankings the more the progression will be increased.
The formula is 10 * d * d where d equals the difference in
ranking between the activity and the user.

Logic Examples:
If a user ranked -8 completes an activity ranked -7 they will receive 10
progress
If a user ranked -8 completes an activity ranked -6 they will receive 40
progress
If a user ranked -8 completes an activity ranked -5 they will receive 90
progress
If a user ranked -8 completes an activity ranked -4 they will receive 160
progress, resulting in the user being upgraded to rank -7 and having earned
60 progress towards their next rank
If a user ranked -1 completes an activity ranked 1 they will receive 10
progress (remember, zero rank is ignored)

Code Usage Examples:
user = User()
user.rank # => -8
user.progress # => 0
user.inc_progress(-7)
user.progress # => 10
user.inc_progress(-5) # will add 90 progress
user.progress # => 0 # progress is now zero
user.rank # => -7 # rank was upgraded to -7
Note:
Codewars no longer uses this algorithm for its own ranking system.
It uses a pure Math based solution that gives consistent results no matter what
order a set of ranked activities are completed at.
'''
def check_progress(current_rank, activity_rank):l
    current_progress = 0
    if activity_rank > 8:
        raise ValueError('Rank too high')
    if activity_rank == 0:
        raise ValueError('Rank cannot be zero')
    if activity_rank < -8:
        raise ValueError('Rank too low')
    if current_rank == 8:
        current_rank = 8
        current_progress = 0
    else:
        if activity_rank < current_rank:
            a = current_rank - activity_rank
            if current_rank < 0 and activity_rank > 0:
                a = a - 1
            if a < -1:
                current_progress = current_progress + 0
            else:
                current_progress = current_progress + 1
        elif activity_rank == current_rank:
            current_progress = current_progress + 3
        else:
            if activity_rank == 1 and current_rank == -1:
                d = 1
            else:
                d = current_rank - activity_rank
            inc = (10 * d * d)
            current_progress = current_progress + inc
        while current_progress >= 100:
            current_progress = current_progress - 100
            if current_rank == -1:
                current_rank = 1
            elif current_rank == 8:
                current_rank = 8
                current_progress = 0
            else:
                current_rank = current_rank + 1
    return current_rank, current_progress


class User:
    def __init__(self):
        self.rank = -8
        self.progress = 0

    def rank(self):
        return self.rank
    def set_rank(self, rank):
        self.rank = rank
    def progress(self):
        print(self.progress,self.rank)
        return self.progress

    def inc_progress(self, activity_rank):
        if activity_rank > 8:
            raise ValueError('Rank too high')
        if activity_rank == 0:
            raise ValueError('Rank cannot be zero')
        if activity_rank < -8:
            raise ValueError('Rank too low')
        if self.rank == 8:
            self.rank = 8
            self.progress = 0
        else:
            if activity_rank < self.rank:
                a = self.rank - activity_rank
                if self.rank < 0 and activity_rank > 0:
                    a = a - 1
                if a < -1:
                    self.progress = self.progress + 0
                else:
                    self.progress = self.progress + 1
            elif activity_rank == self.rank:
                self.progress = self.progress + 3
            else:
                if activity_rank == 1 and self.rank == -1:
                    d = 1
                else:
                    d = self.rank - activity_rank
                inc = (10 * d * d)
                self.progress = self.progress + inc
            while self.progress >= 100:
                self.progress = self.progress - 100
                if self.rank == -1:
                    self.rank = 1
                elif self.rank == 8:
                    self.rank = 8
                    self.progress = 0
                else:
                    self.rank = self.rank + 1

def main():
    """ This is the main routine for the program """
    print("Starting the sequence:")
    sequence = (3, 3, 1, 3, 3, -4, 6, -1, 6, 3)
    user = User()
    test = 0
    # user.set_rank(-1)
    c_rank = -8
    for item in sequence:
        print(check_progress(c_rank, item))
        test += 1


if __name__ == '__main__':
    main()
