<template>
    <ContentWrapper>
        <div class="content-heading">
            <div>SweetAlert
                <small>A Beautiful Replacement For Javascript's "alert"</small>
            </div>
        </div>
        <div class="container-fluid">
            <h4 class="page-header mt-0">Usage examples</h4>
            <div class="row">
                <div class="col-lg-9 col-xl-6">
                    <p>A basic message</p>
                </div>
                <div class="col-lg-3 col-xl-6">
                    <p>
                        <button type="button" class="btn btn-primary" @click="swalDemo1()" >Try me!</button>
                    </p>
                </div>
            </div>
            <div class="row">
                <div class="col-lg-9 col-xl-6">
                    <p>A title with a text under</p>
                </div>
                <div class="col-lg-3 col-xl-6">
                    <p>
                        <button type="button" class="btn btn-primary" @click="swalDemo2()" >Try me!</button>
                    </p>
                </div>
            </div>
            <div class="row">
                <div class="col-lg-9 col-xl-6">
                    <p>A success message!</p>
                </div>
                <div class="col-lg-3 col-xl-6">
                    <p>
                        <button type="button" class="btn btn-primary" @click="swalDemo3()" >Try me!</button>
                    </p>
                </div>
            </div>
            <div class="row">
                <div class="col-lg-9 col-xl-6">
                    <p>A warning message, with a function attached to the &quot;Confirm&quot;-button</p>
                </div>
                <div class="col-lg-3 col-xl-6">
                    <p>
                        <button type="button" class="btn btn-primary" @click="swalDemo4()" >Try me!</button>
                    </p>
                </div>
            </div>
            <div class="row">
                <div class="col-lg-9 col-xl-6">
                    <p>... and by passing a parameter, you can execute something else for &quot;Cancel&quot;.</p>
                </div>
                <div class="col-lg-3 col-xl-6">
                    <p>
                        <button type="button" class="btn btn-primary" @click="swalDemo5()" >Try me!</button>
                    </p>
                </div>
            </div>
        </div>
    </ContentWrapper>
</template>
<script>
    import swal from 'sweetalert2'

    export default {
        name: 'Sweetalert',
        methods: {
            swalDemo1() {
                swal({
                    title: "Here's a message!",
                    heightAuto: false
                })
            },
            swalDemo2() {
                swal({
                    title: "Here's a message!",
                    text: "It's pretty, isn't it?",
                    heightAuto: false
                })
            },
            swalDemo3() {
                swal({
                    title: "Good job!",
                    text: "You clicked the button!",
                    type: "success",
                    heightAuto: false
                })
            },
            swalDemo4() {
                swal({
                        title: "Are you sure?",
                        text: "You will not be able to recover this imaginary file!",
                        type: "warning",
                        showCancelButton: true,
                        confirmButtonColor: "#DD6B55",
                        confirmButtonText: "Yes, delete it!",
                        heightAuto: false
                    }).then((result) => {
                        if(result.value)
                            swal({
                                title: "Deleted!",
                                text: "Your imaginary file has been deleted.",
                                type: "success",
                                heightAuto: false
                            });
                    });
            },
            swalDemo5() {
                swal({
                    title: "Are you sure?",
                    text: "You will not be able to recover this imaginary file!",
                    type: "warning",
                    showCancelButton: true,
                    confirmButtonColor: "#DD6B55",
                    confirmButtonText: "Yes, delete it!",
                    cancelButtonText: "No, cancel plx!",
                    heightAuto: false
                }).then((result) => {
                    if (result.value) {
                        swal({
                            title: "Deleted!",
                            text: "Your imaginary file has been deleted.",
                            type: "success",
                            heightAuto: false
                        });
                    } else {
                        swal({
                            title: "Cancelled",
                            text: "Your imaginary file is safe :)",
                            type: "error",
                            heightAuto: false
                        });
                    }
                });
            },
        }
    }
</script>
