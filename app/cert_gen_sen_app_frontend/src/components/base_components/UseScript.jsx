import { useEffect } from "react";

export const UseScript = (url) => {
  useEffect(() => {
    const script = document.createElement("script");

    script.src = url;
    script.type = "text/babel";
    script.async = false;

    document.body.appendChild(script);

    return () => {
      document.body.removeChild(script);
    };
  }, [url]);
};
