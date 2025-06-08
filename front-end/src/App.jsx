import React, { useEffect } from "react";
import { useState } from "react";
import RootContext from "./providers/root";
import { HomePage, LandingPage } from "./pages";
export const PageName = "results" | "loading" | "home";

function App() {
    const [currentPage, setCurrentPage] = useState(PageName);

    // Root page navigation setup.
    const renderPage = () => {
        switch (currentPage) {
        case "home":
            return <HomePage />;
        default:
            return <LandingPage />;
        }
    }

    return (
        <div>
           <RootContext.Provider value={{
                setCurrentPage,
            }}>
                {renderPage()}
            </RootContext.Provider>
        </div>
    );
}

export default App;
