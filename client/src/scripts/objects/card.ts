export default class Card extends Phaser.GameObjects.Image {
    faceUp: boolean = false;

    constructor(scene, x, y, angle=0) {
        super(scene, x, y, "cards", "back");

        scene.add.existing(this);
        this.setInteractive();
        this.setScale(0.3);
        this.angle = angle;

        //this.on("pointerdown", (pointer) => this.move());
    }
    flip(cardName?: string) {
        //  Will contain the top-most Game Object (in the display list)

        if (cardName) {
            this.setTexture("cards", cardName);
            this.faceUp = true;
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
