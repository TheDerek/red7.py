import PhaserLogo from "../objects/phaserLogo"
import FpsText from "../objects/fpsText"
import Card from "../objects/card"

export default class MainScene extends Phaser.Scene {
  fpsText: FpsText
  frames: string[]

  constructor() {
    super({ key: "MainScene" })
  }

  create() {
    this.fpsText = new FpsText(this)

    // display the Phaser.VERSION
    this.add
      .text(this.cameras.main.width - 15, 15, `Phaser v${Phaser.VERSION}`, {
        color: "#000000",
        fontSize: "24px"
      })
      .setOrigin(1, 0)

    var cardNames = this.textures.get("cards").getFrameNames().slice(0, -1);
    console.log(cardNames);
    new Card(this, 100, 500, "v3");
  }

  update() {
    this.fpsText.update()
  }
}
