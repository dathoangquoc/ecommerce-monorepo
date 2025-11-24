'use client'

import { ReactNode } from "react";
import { CartProvider } from "./CartContext";

export default function CatalogLayout({ children }: { children: ReactNode }) {
    return (
        <CartProvider>
            { children }
        </CartProvider>
    )
}