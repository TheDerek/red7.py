import { store, CardName } from "../store";

function createPlayCardAction(card: Card) {
    return function(dispatch) {
        card.scene.tweens.add({
            targets: card,
            x: { value: 1100, duration: 1500, ease: 'Power2' },
            y: { value: 0, duration: 1500, ease: 'Power2' },
            onComplete: () => dispatch({type: "PLAY_CARD", card: card.cardName})
            //onComplete: dispatch({type: "PLAY_CARD", card: card.cardName})
        });
    }
}

export default class Card extends Phaser.GameObjects.Image {
    faceUp: boolean = false;
    cardName: CardName;

    constructor(scene, x, y, angle=0) {
        super(scene, x, y, "cards", "back");

        scene.add.existing(this);
        this.setInteractive();
        this.setScale(0.3);
        this.angle = angle;

        this.on("pointerdown", this.onClick);
    }

    onClick() {
        console.log("Clicked! " + this.cardName);
        if (this.cardName) {
            // @ts-ignore
            store.dispatch(createPlayCardAction(this));
        }
    }

    flip(cardName?: CardName) {
        //  Will contain the top-most Game Object (in the display list)
        if (cardName) {
            this.setTexture("cards", cardName);
            this.faceUp = true;
            this.cardName = cardName;
        }
        else {
            this.setTexture("cards", "back");
            this.faceUp = false;
        }
    }

    move() {
        this.scene.tweens.add({
            targets: this,
            x: { value: 1100, duration: 1500, ease: 'Power2' },
        });
    }
}
