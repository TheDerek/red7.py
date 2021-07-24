import FpsText from '../objects/fpsText'
import Card from '../objects/card'

export default class MainScene extends Phaser.Scene {
  fpsText: FpsText
  frames: string[]

  constructor() {
    super({ key: 'MainScene' })
  }

  create() {
    this.fpsText = new FpsText(this)

    // display the Phaser.VERSION
    this.add
      .text(this.cameras.main.width - 15, 15, `Phaser v${Phaser.VERSION}`, {
        color: '#000000',
        fontSize: '24px'
      })
      .setOrigin(1, 0)

    var cardNames = this.textures.get('cards').getFrameNames().slice(0, -1)
    // @ts-ignore
    Phaser.Actions.Shuffle(cardNames)
    console.log(cardNames)

    var cards: Card[] = cardNames.map(
      name => new Card(this, Phaser.Math.FloatBetween(100, 150), Phaser.Math.FloatBetween(500, 550))
    )

    cards.reverse().forEach((card, index) => {
      this.tweens.add({
        targets: card,
        x: { value: 1100, duration: 1500, ease: 'Power2' },
        delay: index * 100,
        onComplete: () => console.log("Completed! " + card)
      })
    })
  }

  update() {
    this.fpsText.update()
  }
}
