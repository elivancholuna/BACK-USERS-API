package com.uap.user.controller;

import com.uap.user.dto.model.UserResponse;
import com.uap.user.usecase.UserService;

import static org.mockito.ArgumentMatchers.any;
import static org.mockito.Mockito.when;

import java.util.List;
import java.util.Optional;

import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;
import org.junit.jupiter.api.extension.ExtendWith;
import org.mockito.InjectMocks;
import org.mockito.Mock;
import org.mockito.junit.jupiter.MockitoExtension;
import org.springframework.http.ResponseEntity;
import static org.assertj.core.api.Assertions.assertThat;
import static org.assertj.core.api.Assertions.assertThatThrownBy;
import static org.mockito.Mockito.verify;

@ExtendWith(MockitoExtension.class)
public class UserControllerTest {
    
    @Mock
    private UserService userService;

    @InjectMocks
    private UserController controller;

    @Test
    @DisplayName("Test nro 1 - get user")
    void getAllUsers_success() {
        when(userService
            .findAllUsers(any()))
            .thenReturn(List.of());

        ResponseEntity<List<UserResponse>> response = controller.getAllUsers();

        verify(userService).findAllUsers(any());
        assertThat(response.getBody().isEmpty()).isTrue();


    }

    @Test
    void getAllUser_Fail(){
        when(userService.findAllUsers(any())).thenThrow(RuntimeException.class);

        ResponseEntity<List<UserResponse>> response = controller.getAllUsers();


    }

    //J+,
}
