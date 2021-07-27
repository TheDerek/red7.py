import { createStore, Store, applyMiddleware, compose } from "redux";
import thunk from "redux-thunk";

export type CardName =
    | "v1"
    | "i1"
    | "b1"
    | "g1"
    | "y1"
    | "o1"
    | "r1"
    | "v2"
    | "i2"
    | "b2"
    | "g2"
    | "y2"
    | "o2"
    | "r2"
    | "v3"
    | "i3"
    | "b3"
    | "g3"
    | "y3"
    | "o3"
    | "r3"
    | "v4"
    | "i4"
    | "b4"
    | "g4"
    | "y4"
    | "o4"
    | "r4"
    | "v5"
    | "i5"
    | "b5"
    | "g5"
    | "y5"
    | "o5"
    | "r5"
    | "v6"
    | "i6"
    | "b6"
    | "g6"
    | "y6"
    | "o6"
    | "r6"
    | "v7"
    | "i7"
    | "b7"
    | "g7"
    | "y7"
    | "o7"
    | "r7";

const PLAY_CARD = "PLAY_CARD";
const DISCARD_CARD = "DISCARD_CARD";
const ADD_CARD = "ADD_CARD";

interface PlayCardAction {
    type: typeof PLAY_CARD;
    card: CardName;
}

interface DiscardCardAction {
    type: typeof DISCARD_CARD;
    card: CardName;
}

interface AddCardAction {
    type: typeof ADD_CARD;
    card: CardName;
}

type Actions = PlayCardAction | DiscardCardAction | AddCardAction;


type Opponent = {
    palette: CardName[];
    hand: integer;
};

type GameState = {
    hand: CardName[];
    palette: CardName[];
    canvas: CardName;
    opponents: Opponent[];
};

const initialState: GameState = {
    hand: ["i5", "b5", "o6"],
    palette: ["b4", "g5"],
    canvas: "r7",
    opponents: [
        {
            palette: ["r7", "b3"],
            hand: 7,
        },
    ],
};

function reducer(state: GameState = initialState, action: Actions): GameState {
    switch (action.type) {
        case PLAY_CARD:
            let handIndex = state.hand.indexOf(action.card);
            let newHand = [...state.hand];
            newHand.splice(handIndex, 1);
            return {
                ...state,
                hand: newHand,
                palette: [...state.palette, action.card],
            };
        case DISCARD_CARD:
            break;
        case ADD_CARD:
            return {
                ...state,
                hand: [...state.hand, action.card],
            };
    }

    return state;
}

export const store: Store<GameState, Actions> = createStore(
    reducer,
    compose(
        applyMiddleware(thunk),
        // @ts-ignore
        window.__REDUX_DEVTOOLS_EXTENSION__ &&
        // @ts-ignore
            window.__REDUX_DEVTOOLS_EXTENSION__()
    )
);
