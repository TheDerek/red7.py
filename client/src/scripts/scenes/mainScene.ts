import FpsText from "../objects/fpsText";
import Card from "../objects/card";
import { store } from "../store";

export default class MainScene extends Phaser.Scene {
    fpsText: FpsText;
    frames: string[];
    store: typeof store;
    cardNames: string[];
    hand: Phaser.GameObjects.Group;
    opponents: Phaser.GameObjects.Group;
    deck: Card;
    canvas: Card;
    spacebar;

    constructor() {
        super({ key: "MainScene" });
        this.store = store;
        this.store.subscribe(this.renderStatechange.bind(this));
    }

    renderStatechange() {
        const newState = this.store.getState();

        // Render the players hand
        this.hand.clear(true, true);
        var margin = 10.0;
        var width = this.textures.get("cards").frames["r1"].width * 0.3;
        var height = this.textures.get("cards").frames["r1"].height * 0.3;
        var iX =
            this.cameras.main.width / 2.0 -
            ((newState.hand.length - 1) * (width + margin)) / 2.0;
        let y = this.cameras.main.height - margin * 3;

        newState.hand.forEach((cardName, index) => {
            let x = iX + index * (width + margin);
            var card = new Card(this, x, y);
            card.flip(cardName);
            this.hand.add(card);
        });

        iX =
            this.cameras.main.width / 2.0 -
            ((newState.palette.length - 1) * (width + margin)) / 2.0;
        y = this.cameras.main.height - width * 1.5 - margin * 3;

        newState.palette.forEach((cardName, index) => {
            let x = iX + index * (width + margin);
            var card = new Card(this, x, y);
            card.flip(cardName);
            this.hand.add(card);
        });

        // Render opponents
        this.opponents.clear(true, true);
        // Render hidden hand
        let opponent = newState.opponents[0];
        iX =
            this.cameras.main.width / 2.0 -
            ((opponent.hand - 1) * (width + margin)) / 2.0;
        y = -margin;
        for (let i = 0; i < opponent.hand; i++) {
            let x = iX + i * (width + margin);
            var card = new Card(this, x, y, 180);
            this.opponents.add(card);
        }
        // Render visible palette
        y = width * 1.5;
        iX =
            this.cameras.main.width / 2.0 -
            ((opponent.palette.length - 1) * (width + margin)) / 2.0;
        opponent.palette.forEach((cardName, index) => {
            let x = iX + index * (width + margin);
            var card = new Card(this, x, y, 180);
            card.flip(cardName);
            this.opponents.add(card);
        });

        // Render the deck
        if (this.deck) {
            this.deck.destroy(true);
        }
        this.deck = new Card(
            this,
            this.cameras.main.width / 2.0 -(height + margin)/2.0,
            this.cameras.main.height / 2.0 - 15,
            90
        );

        // Render the canvas
        if (this.canvas) {
            this.canvas.destroy(true);
        }
        this.canvas = new Card(
            this,
            this.cameras.main.width / 2.0 +(height + margin)/2.0,
            this.cameras.main.height / 2.0 - 15,
            90
        );
        this.canvas.flip(newState.canvas);
    }

    create() {
        this.fpsText = new FpsText(this);
        this.hand = this.add.group();
        this.opponents = this.add.group();

        this.renderStatechange();

        this.spacebar = this.input.keyboard.addKey(
            Phaser.Input.Keyboard.KeyCodes.SPACE
        );

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
        if (Phaser.Input.Keyboard.JustDown(this.spacebar)) {
            console.log("JUTS DOWWWN");
            this.store.dispatch({ type: "ADD_CARD", card: "r7" });
        }
    }
}
