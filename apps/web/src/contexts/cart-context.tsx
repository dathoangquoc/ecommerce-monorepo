'use client'

import { createContext, useContext, ReactNode, useReducer } from "react";
import { CartProduct } from "@/types/product";

type CartAction = 
    | {type: "added_item"; product: CartProduct} 
    | {type: "removed_item"; product: CartProduct} 


// init with type and empty default values
const CartContextValue = createContext<CartProduct[]>([]);
const CartDispatchContext = createContext<React.Dispatch<CartAction>>(() => {});

export function CartProvider({ children }: { children: ReactNode }) {
    const [cart, cartDispatch] = useReducer(cartReducer, []);
    
    return (
        <CartContextValue.Provider value={cart}>
            <CartDispatchContext.Provider value={cartDispatch}>
                {children}
            </CartDispatchContext.Provider>
        </CartContextValue.Provider>
    );
}

export function useCart() {
    return useContext(CartContextValue);
}

export function useCartDispatch() {
    return useContext(CartDispatchContext);
}

function cartReducer(state: CartProduct[], action: CartAction): CartProduct[] {
    const existing = state.find(p => p.id === action.product.id);
    switch (action.type) {
        case "added_item": {
            if (existing) {
                return state.map(p => 
                    p.id === action.product.id
                        ? {...p, count: p.count + 1}
                        : p
                )
            }
            return [...state, action.product]
        }
        case "removed_item": {
            if (existing && existing.count > 1) {
                return state.map(p => 
                    p.id === action.product.id
                        ? {...p, count: p.count - 1}
                        : p
                )
            }

            return state.filter(p => p.id !== action.product.id)
        }
        default: {
            throw new Error("Unknown action type: " + (action as any).type);
        }
    }
}