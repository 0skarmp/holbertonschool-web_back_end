export default function getResponseFromAPI() {
    return new Promise((resolve, reject) => {
      if (success) { 
        resolve({
          status: 200,
          body: "success"
        });
      } else {
        reject("The fake API is not working currently");
      }
    });
  }
