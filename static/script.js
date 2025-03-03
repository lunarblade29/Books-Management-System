document.addEventListener("DOMContentLoaded", function () {
    document.getElementById("bookForm").addEventListener("submit", function (event) {
        event.preventDefault(); // Prevent form from reloading

        let formData = new FormData(this);

        fetch("/", {
            method: "POST",
            body: formData
        })
        .then(response => response.json())
        .then(data => {
            if (data.status === "success") {
                Swal.fire({
                    title: "Success!",
                    text: data.message,
                    icon: "success",
                    confirmButtonText: "OK"
                }).then(() => {
                    document.getElementById("bookForm").reset(); // Clear form
                });
            } else {
                Swal.fire({
                    title: "Error!",
                    text: "Something went wrong.",
                    icon: "error",
                    confirmButtonText: "Try Again"
                });
            }
        })
        .catch(error => {
            console.error("Error:", error);
            Swal.fire({
                title: "Error!",
                text: "Unable to submit. Please try again.",
                icon: "error",
                confirmButtonText: "OK"
            });
        });
    });
});
