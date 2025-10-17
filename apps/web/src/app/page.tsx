import './globals.css'

export default async function Page() {
  let message = "API offline..."

  try {
    const data = await fetch("http://127.0.0.1:8000")
    message = await data.json()
  } catch (error) {
    console.log(error)
  }

  return (
    <>
    <h1>{message}</h1>
    <form action="">
          <div>
              <label htmlFor="email">Email</label>
              <input type="text" id="email" name="email" placeholder="Email" />
          </div>
          <div>
              <label htmlFor="password">Password</label>
              <input type="text" id="password" name="password" placeholder="Password" />
          </div>
          <button type="submit">Log In</button>
        </form>
    </>
  );
}