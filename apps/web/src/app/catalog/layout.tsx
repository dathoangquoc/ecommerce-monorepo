'use client'

import { ReactNode } from "react";

import { SidebarProvider, SidebarTrigger } from "@/components/ui/sidebar";
import { CartSidebar } from "@/components/ui/cart-sidebar"

import { useCart, useCartDispatch } from "@/contexts/cart-context"

import { CartProduct } from "@/types/product";

import { toast } from "sonner"


export default function CatalogLayout({ children }: { children: ReactNode }) {
    const cart = useCart();
    const cartDispatch = useCartDispatch();
    
    return (
        <SidebarProvider>
            <CartSidebar 
                cart={cart}
                handleAddToCart={(product) => {
                    toast.success(`+1 ${product.name}`)
                    cartDispatch({
                        type: "added_item",
                        product: product
                    })
                }}
                handleRemoveFromCart={(product) => {
                    toast.success(`-1 ${product.name}`)
                    cartDispatch({
                        type: "removed_item",
                        product: product
                    })
                }}
            />
            <SidebarTrigger />
            { children }
        </SidebarProvider>
    )
}