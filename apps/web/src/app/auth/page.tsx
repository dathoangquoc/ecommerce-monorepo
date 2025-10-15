export default function Page() {
    return (
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
    )
}
