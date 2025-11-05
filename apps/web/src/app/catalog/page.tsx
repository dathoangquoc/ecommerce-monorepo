'use client'

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
import { MouseEventHandler, useState } from "react"

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
        "count": 2
    },
    {
        "id": "003",
        "name": "Product 3",
        "image": "/next.svg",
        "price": 300,
        "description": "Lorem ipsum",
        "count": 3
    },
]

interface Product {
    id: string;
    name: string;
    image: string;
    price: number
    description: string;
    count: number
}

export default function Page() {
    const [cart, setCart] = useState<Product[]>([]);

    function handleAddToCart(product: Product) {
        setCart((prevCart) => [...prevCart, product])
    }

    return (
        <main className="flex w-full max-w-xl flex-col gap-6">
            <p>
                {cart.length > 0
                    ? cart.map((product) => product.name).join(", ")
                    : "Cart is empty"
                }
            </p>
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