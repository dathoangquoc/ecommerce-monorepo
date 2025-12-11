export default interface Product {
    id: string;
    name: string;
    image: string;
    price: number
    description: string;
}

export type CartProduct = Product & {
    count: number
}