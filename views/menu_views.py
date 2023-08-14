import json
import sys
sys.path.append('./')
from controllers.json_function import load_tournament
from models.tournament import Tournament
from models.player import Player
from models.game import Game
from models.round import Round
import player_views
import tournament_views 
import time

def main_menu():
    x = 0
    while x == 0:
        print("\nMenu principal: ")
        print("1. Inscription des joueurs à la compétition annuelle")
        print("2. Créer un nouveau tournoi")
        print("3. Reprendre un tournoi en cours")
        print("4. Quitter")
        
        choice = input("Choisissez un des options parmi les suivantes(1,2,3,4): ")
        
        if choice == "1":
            player_views.players_for_competition()
        elif choice == "2":
            tournament = tournament_views.create_tournament()
            for player in tournament.players:
                print(player)
            tournament.save_to_json(f"./tournois/{tournament.name}")
            tournament.shuffle_players()
            print("Le tournoi à été crée avec succés")
            start_or_pass = input("Si vous souhaitez démarrer le tournoi tapez 1 entrer une touche: ")
            if start_or_pass == "1":
                tournament_views.play_tournament(tournament)
        elif choice == "3":
            tournament_name = input("Entrer le nom du tournoi à reprendre: ")
            tournament = load_tournament(f"./tournois/{tournament_name}")
            if tournament is not None:
                tournament_views.play_tournament(tournament)
            else:
                print("Tournoi non trouvé")
        elif choice == "4":
            print("Au revour")
            x = 1
        else:
            print("Option invalide veuillez choisir entre 1, 2, 3 ou 4")
                
main_menu()