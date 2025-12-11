'use client'

import { 
    Sidebar, 
    SidebarContent, 
} from "@/components/ui/sidebar";

import { CartProduct } from "@/types/product";

interface CartSidebarProps {
    cart: CartProduct[];
    handleAddToCart: (product: CartProduct) => void;
    handleRemoveFromCart: (product: CartProduct) => void;
}

function CartSidebar({ 
    cart, 
    handleAddToCart, 
    handleRemoveFromCart 
}: CartSidebarProps): React.JSX.Element {
    return (
        <Sidebar>
            <SidebarContent>
            <ul>
                {cart.length > 0 ?
                    cart.map((product: CartProduct) => (
                        <li key={product.id}>
                            {product.name} | {product.count}
                            <button onClick={() => {
                                handleRemoveFromCart(product)
                            }}> Remove </button>
                        </li>
                    ))
                    : "Cart is empty"
                }
            </ul>
            </SidebarContent>
        </Sidebar>
    )
}

export { CartSidebar }