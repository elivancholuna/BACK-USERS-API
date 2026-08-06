package com.uap.user.dto.model;
import com.fasterxml.jackson.annotation.JsonIgnoreProperties;
import com.fasterxml.jackson.annotation.JsonProperty;
import java.util.List;

@JsonIgnoreProperties(ignoreUnknown = true)
public class UserApiResponse {
    public int page;
    @JsonProperty("per_page")
    public int perPage;
    public int total;
    @JsonProperty("total_pages")
    public int totalPages;
    public List<User> data;
}

@JsonIgnoreProperties(ignoreUnknown = true)
class User {
    public int id;
    public String email;
    @JsonProperty("first_name")
    public String firstName;
    @JsonProperty("last_name")
    public String lastName;
    public String avatar;
}

