#include <iostream>
#include <ctime>
#include <cstdlib>
using namespace std;

int main() {
    cout << "Selamat datang di Attack On Monster" << endl;
    cout << "Langkah - langkah permainan: " << endl;
    cout << "1. Player and monster have same life = 21" << endl;
    cout << "2. If the player is correct in guessing the number, the player will get additional lives = 3 and can attack monsters with damage = 2" << endl;
    cout << "3. If the player guesses the wrong number, the player will receive damage = 2" << endl;
    cout << "4. The player is declared victorious, if until the end of the game the player's life is more than the monster" << endl;
    cout << "5. If the player enters a guessed number more than 10, it will be considered a loss" << endl;

    int count = 10;
    int playerLife = 21;
    int monsterLife = 21;
    int extraLife = 3;
    int damage = 2;
    int inputNumber;

    while(count != 0) {
        cout << "\n" << endl;
        srand(static_cast<unsigned int>(time(0)));
        int angkaAcak = rand() % 10 + 1;

        cout << "Enter your guess (1-10): ";
        cin >> inputNumber;

        if (inputNumber > 10){
            cout << "\n" << endl;
            cout << "You enter number that greater than 10" << endl;
            break;
        } else {
            cout << "Your guess: " << inputNumber << endl;
            cout << "Random number: " << angkaAcak << "\n" << endl;
            
            if (inputNumber == angkaAcak) {
                cout << "Your guess is right!!" << endl;
                playerLife += extraLife; 
                monsterLife -= damage;
            }  
            else {
                if (inputNumber > angkaAcak)
                    cout << "Your guess is too big" << endl;
                else
                    cout << "Your guess is too small" << endl;
                playerLife -= damage;
            }
                
            cout << "\n";
            cout << "Monster life: " << monsterLife << endl;
            cout << "Player life: " << playerLife << endl;
            count--;
            if(count != 0){
                cout << "Remaining playing opportunities " << count << " again" << endl;
                cout << "===================================== \n" << endl;
            }
            else {
                cout << "The opportunity to play is end" << endl;
                cout << "===================================== \n" << endl;
            }
        }
    }
    
    if (count != 0) {
        cout << "=========" << endl;
        cout << "GAME OVER" << endl;
        cout << "=========" << endl;
    } else {
        if (monsterLife == playerLife) {
            cout << "==================" << endl;
            cout << "Series Match" << endl;
            cout << "==================" << endl;
        }
        else if (monsterLife > playerLife) {
            cout << "=============================" << endl;
            cout << "You lose and Monster win" << endl;
            cout << "=============================" << endl;
        }
        else {
            cout << "=========================" << endl;
            cout << "Congrats you win! yeyy" << endl;
            cout << "=========================" << endl;
        }
    }

}