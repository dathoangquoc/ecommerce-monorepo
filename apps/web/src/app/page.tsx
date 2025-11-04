import './globals.css'

import {
  Field,
  FieldDescription,
  FieldGroup,
  FieldLabel,
  FieldSet,
} from "@/components/ui/field"
import { Input } from "@/components/ui/input"
import { Button } from "@/components/ui/button"

export default async function Page() {
  let message = "API offline..."

  // try {
  //   const data = await fetch("http://127.0.0.1:8000")
  //   message = await data.json()
  // } catch (error) {
  //   console.log(error)
  // }

  return (
    <main className='mx-auto max-w-6xl p-5 border'>
      <h1 className=''>{message}</h1>
      <div className="w-full max-w-md">
      <FieldSet>
        <FieldGroup>
          <Field>
            <FieldLabel htmlFor="username">Username</FieldLabel>
            <Input id="username" type="text" placeholder="Max Leiter" />
            <FieldDescription>
              Choose a unique username for your account.
            </FieldDescription>
          </Field>
          <Field>
            <FieldLabel htmlFor="password">Password</FieldLabel>
            <FieldDescription>
              Must be at least 8 characters long.
            </FieldDescription>
            <Input id="password" type="password" placeholder="********" />
          </Field>
        </FieldGroup>
        <Button type="submit">Submit</Button>
      </FieldSet>
    </div>
    </main>
  );
}