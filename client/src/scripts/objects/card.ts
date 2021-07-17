export default class Card extends Phaser.GameObjects.Image {
    faceUp: boolean = true;
    cardName: string;

    constructor(scene, x, y, cardName: string) {
        super(scene, x, y, "cards", cardName);

        scene.add.existing(this);
        this.setInteractive();
        this.setScale(0.3);
        this.cardName = cardName;

        this.on("pointerdown", (pointer) => this.flip());
    }
    flip() {
        console.log("Flippy flippy?");
        //  Will contain the top-most Game Object (in the display list)
        this.scene.tweens.add({
            targets: this,
            x: { value: 1100, duration: 1500, ease: 'Power2' },
        });
        if (this.faceUp) {
            this.setTexture("cards", "back");
        } else {
            console.log(this.cardName);
            this.setTexture("cards", this.cardName);
        }

        this.faceUp = !this.faceUp;

    }
}
