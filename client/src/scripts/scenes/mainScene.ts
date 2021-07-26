import FpsText from "../objects/fpsText";
import Card from "../objects/card";
import { store } from "../store";

export default class MainScene extends Phaser.Scene {
    fpsText: FpsText;
    frames: string[];
    store: typeof store;
    cardNames: string[];
    hand: Phaser.GameObjects.Group;

    constructor() {
        super({ key: "MainScene" });
        this.store = store;
        this.store.subscribe(this.renderStatechange);
    }

    renderStatechange() {
        const newState = this.store.getState();
        console.log("Rendering state change!");

        // Render the players hand
        var margin = 10.0;
        var width = this.textures.get("cards").frames["r1"].width * 0.3;
        var height = this.textures.get("cards").frames["r1"].height * 0.3;
        var iX = (this.cameras.main.width / 2.0) - (((newState.hand.length - 1) * (width + margin) / 2.0));
        let y = this.cameras.main.height - margin - height/2.0;

        console.log(newState.hand.length * (width + margin));
        newState.hand.forEach((cardName, index) => {
            let x = iX + index * (width + margin);
            var card = new Card(this, x, y);
            card.flip(cardName);
            this.hand.add(card);
        });
    }

    create() {
        this.fpsText = new FpsText(this);
        this.hand = this.add.group();

        this.renderStatechange();

        // display the Phaser.VERSION
        this.add
            .text(
                this.cameras.main.width - 15,
                15,
                `Phaser v${Phaser.VERSION}`,
                {
                    color: "#000000",
                    fontSize: "24px",
                }
            )
            .setOrigin(1, 0);

        // this.cardNames = this.textures.get("cards").getFrameNames().slice(0, -1);
        // // @ts-ignore
        // Phaser.Actions.Shuffle(this.cardNames);

        // var cards: Card[] = this.cardNames.map(
            // (name) =>
                // new Card(
                    // this,
                    // Phaser.Math.FloatBetween(100, 150),
                    // Phaser.Math.FloatBetween(500, 550)
                // )
        // );
//
        // cards.reverse().forEach((card, index) => {
            // this.tweens.add({
                // targets: card,
                // x: { value: 1100, duration: 1500, ease: "Power2" },
                // delay: index * 100,
                // onComplete: () => console.log("Completed! " + card),
            // });
        // });
    }

    update() {
        this.fpsText.update();
    }
}
