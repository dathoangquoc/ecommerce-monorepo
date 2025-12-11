import { CartProduct } from "@/types/product"

import Image from "next/image"

import {
  Item,
  ItemContent,
  ItemDescription,
  ItemGroup,
  ItemHeader,
  ItemTitle,
} from "@/components/ui/item"

import { Button } from "@/components/ui/button"

import { useContext } from "react"
import { UserContext } from "../../contexts/user-context"

import { toast } from "sonner"

import { useCartDispatch } from "@/contexts/cart-context"

const products = [
    {
        "id": "001",
        "name": "Product 1",
        "image": "/next.svg",
        "price": 100,
        "description": "Lorem ipsum",
        "count": 1
    },
    {
        "id": "002",
        "name": "Product 2",
        "image": "/next.svg",
        "price": 200,
        "description": "Lorem ipsum",
        "count": 1
    },
    {
        "id": "003",
        "name": "Product 3",
        "image": "/next.svg",
        "price": 300,
        "description": "Lorem ipsum",
        "count": 1
    },
]


export default function Page() {
    // FIXME
    const user = useContext(UserContext);
    const cartDispatch = useCartDispatch();

    const handleAddToCart=(product: CartProduct) => {
        toast.success(`+1 ${product.name}`)
        cartDispatch({
            type: "added_item",
            product: product
        })
    }
    const handleRemoveFromCart=(product: CartProduct) => {
        toast.success(`-1 ${product.name}`)
        cartDispatch({
            type: "removed_item",
            product: product
        })
    }

    return (
        <main className="flex w-full max-w-xl flex-col gap-6 p-6">
            <h1>Current User: {user.name}</h1>
            <ItemGroup className="grid grid-cols-3 gap-4">
                {products.map((product) => (
                    <Item key={product.id} variant="outline">
                    <ItemHeader>
                    <Image
                        src={product.image}
                        alt={product.name}
                        width={128}
                        height={128}
                        className="aspect-square w-full rounded-sm object-cover"
                        />
                    </ItemHeader>
                    <ItemContent>
                        <ItemTitle>{product.name}</ItemTitle>
                        <ItemDescription>{product.description}</ItemDescription>
                    </ItemContent>
                        <Button onClick={() => handleAddToCart(product)}>Add to Cart</Button>
                </Item>
                ))}
            </ItemGroup>
        </main>
    )
}
