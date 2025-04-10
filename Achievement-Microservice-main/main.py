from flask import Flask, request, jsonify

app = Flask(__name__)

# Dummy storage for achievements (for testing purposes)
achievements = []
opponents_defeated = []


@app.route('/pokemon_added', methods=['POST'])
def pokemon_added():
    data = request.json
    pokemon_inventory = data.get('pokemon_inventory')

    if pokemon_inventory is None:
        return jsonify({"error": "Pokemon inventory data is required."}), 400

    # Check if the player has just added their first Pokemon
    if len(achievements) == 0:
        # Add achievement for adding the first Pokemon
        achievements.append("Add First Pokemon")
        print("Achievements: ", achievements)
        return jsonify({"message": "New Achievement: Add First Pokemon"}), 200


@app.route('/battle_completed', methods=['POST'])
def battle_completed():
    data = request.json
    opponent_name = data.get('opponent_name')

    if opponent_name is None:
        return jsonify({"error": "Opponent information is required."}), 400

    opponents_defeated.append(opponent_name)
    print("Opponents defeated: ", opponents_defeated)

    # Check if the player has just defeated their first opponent
    if len(opponents_defeated) == 1:
        # Add opponent to list of those the player has defeated
        achievements.append("Defeat First Opponent")
        print("Achievements: ", achievements)
        return jsonify({"message": "New Achievement: Defeat First Opponent"}), 200
    else:
        return jsonify({"message": "Opponents defeated list updated."}), 200


@app.route('/achievements', methods=['GET'])
def get_achievements():
    return jsonify({"achievements": achievements, "opponents_defeated": opponents_defeated}), 200


if __name__ == '__main__':
    app.run(debug=True)


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
