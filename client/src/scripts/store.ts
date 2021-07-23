import { createStore, Store } from 'redux';

const PLAY_CARD = "PLAY_CARD";
const DISCARD_CARD = "DISCARD_CARD";

type Card = "v1" | "i1" | "b1" | "g1" | "y1" | "o1" | "r1" | "v2" | "i2" | "b2" | "g2" | "y2" | "o2" | "r2" | "v3" | "i3" | "b3" | "g3" | "y3" | "o3" | "r3" | "v4" | "i4" | "b4" | "g4" | "y4" | "o4" | "r4" | "v5" | "i5" | "b5" | "g5" | "y5" | "o5" | "r5" | "v6" | "i6" | "b6" | "g6" | "y6" | "o6" | "r6" | "v7" | "i7" | "b7" | "g7" | "y7" | "o7" | "r7";



interface PlayCardAction {
    type: typeof PLAY_CARD,
    card: Card
}

interface DiscardCardAction {
    type: typeof DISCARD_CARD,
    discardCard: Card
}

type Actions =
    | PlayCardAction
    | DiscardCardAction;

type GameState = {
    hand: Card[]
    palette: Card[]
}

const initialState: GameState = {
    hand: ["i5", "b5", "o6"],
    palette: ["b4", "g5"]
};

function reducer(state: GameState = initialState, action: Actions): GameState {
    switch (action.type) {
        case PLAY_CARD:
            break;
        case DISCARD_CARD:
            break;
    }

    return state;
}

const store: Store<GameState, Actions> = createStore(reducer);
